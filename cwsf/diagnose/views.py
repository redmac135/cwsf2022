from django.shortcuts import render, redirect
import json
import re

from numpy import matrix
from .forms import DiagnoseForm, GenelabForm
from django.views.generic import View
from django.http.response import HttpResponse
from cwsf.settings import BASE_DIR

import os
import mimetypes
from .utils import parse_file, geneNames, getRGBA, linear_color_map
from .ai import predict


# Create your views here.


class DiagnoseView(View):
    template_names = ["diagnose/diagnose_form.html", "diagnose/diagnose_results.html"]
    form_class = DiagnoseForm

    examples = [("1", "example2.txt"), ("2", "example3.txt"), ("3", "example4.txt")]

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(
            request, self.template_names[0], {"form": form, "examples": self.examples}
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if not form.is_valid():
            return render(
                request,
                self.template_names[0],
                {"form": form, "examples": self.examples},
            )
        try:
            results = parse_file(request.FILES["upload"])
            preds = predict(results)
            matrix_colors = linear_color_map(results).tolist()
        except ValueError:
            return redirect("valueError")
        form.save()
        labels = [x[0] for x in preds]
        output = [x[1] for x in preds]
        colors = [getRGBA(x) for x in output]
        return render(
            request,
            self.template_names[1],
            {
                "labels": labels,
                "output": output,
                "colors": colors,
                "matrix_data": json.dumps({
                    "gene_names": geneNames,
                    "matrix_colors": matrix_colors,
                }),
            },
        )

examplenames = ["example2.txt", "example3.txt", "example4.txt"]
def exampleView(request, filename:str = ""):
    if filename == "":
        return redirect('home')
    if filename not in examplenames:
        return redirect('home')
    filepath = os.path.join(
        BASE_DIR, "diagnose", "static", "diagnose", "files", filename
    )
    with open(filepath, "rb+") as f:
        f.seek(0)
        data = f.read().decode()
        lines = re.split(r"[\s,]+", data)
    results = list(map(float, lines))
    preds = predict(results)
    matrix_colors = linear_color_map(results).tolist()
    labels = [x[0] for x in preds]
    output = [x[1] for x in preds]
    colors = [getRGBA(x) for x in output]
    return render(
        request,
        "diagnose/diagnose_results.html",
        {
            "labels": labels,
            "output": output,
            "colors": colors,
            "matrix_data": json.dumps({
                "gene_names": geneNames,
                "matrix_colors": matrix_colors,
            }),
        },
    )

def valueError(request):
    return render(request, "diagnose/valueError.html", {})

def downloadFile(request, filename=""):
    if filename == "":
        return redirect('home')
    filepath = os.path.join(
        BASE_DIR, "diagnose", "static", "diagnose", "files", filename
    )
    path = open(filepath, "rb")
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response["Content-Disposition"] = f"attachment; filename={filename}"

    return response

class GenelabView(View):
    template_names = ["diagnose/genelab_form.html", "diagnose/genelab_results.html"]
    form_class = GenelabForm

    examples = [("1", "example2.txt"), ("2", "example3.txt"), ("3", "example4.txt")]

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(
            request, self.template_names[0], {"form": form, "examples": self.examples}
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if not form.is_valid():
            return render(
                request,
                self.template_names[0],
                {"form": form, "examples": self.examples},
            )
        try:
            results = parse_file(request.FILES["upload"])
            preds = predict(results)
            matrix_colors = linear_color_map(results).tolist()
        except ValueError:
            return redirect("valueError")
        form.save()
        labels = [x[0] for x in preds]
        output = [x[1] for x in preds]
        colors = [getRGBA(x) for x in output]
        return render(
            request,
            self.template_names[1],
            {
                "labels": labels,
                "output": output,
                "colors": colors,
                "matrix_data": json.dumps({
                    "gene_names": geneNames,
                    "matrix_colors": matrix_colors,
                }),
            },
        )