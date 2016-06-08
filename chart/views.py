"""
module description
"""
# encoding:utf-8
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def string_to_int_or_float(value):
    try:
        value = float(value.strip())
    except ValueError:
        value = -1
    return value


def get_render_data(chart_type, chart_data):
    """
    get_render_data description
    """
    lines = chart_data.split("\n")

    result = [] if chart_type == "1" else {}
    for line in lines:
        line = line.strip()
        if not line:
            continue

        tmp_list = line.split(",")

        second = tmp_list[-1]
        first = ",".join(tmp_list[0:-1])

        if chart_type == "1":
            result.append([first.strip(), string_to_int_or_float(second)])
        else:
            result[first.strip()] = string_to_int_or_float(second)
    if isinstance(result, list):
        result.sort(key=lambda item: item[1], reverse=True)
    return result


def chart(request):
    chart_type = request.POST['type']
    render_data = get_render_data(chart_type, request.POST['chartdata'])
    return render(request, 'charts.html' if chart_type == "1" else "charts-time.html", {
        "chart_type": chart_type,
        "render_data": render_data

    })
