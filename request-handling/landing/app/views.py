from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()

TEST = 'test'
ORIGINAL = 'original'


def index(request):
    from_landing = request.GET.get('from-landing')
    if from_landing == ORIGINAL:
        counter_click[ORIGINAL] += 1
    elif from_landing == TEST:
        counter_click[TEST] += 1

    return render_to_response('index.html')


def landing(request):
    ab_test_arg = request.GET.get('ab-test-arg', 'original')

    if ab_test_arg == TEST:
        counter_show[TEST] += 1
        return render_to_response('landing_alternate.html')

    counter_show[ORIGINAL] += 1
    return render_to_response('landing.html')


def stats(request):
    try:
        test_indicator = counter_click[TEST] / counter_show[TEST]
        original_indicator = counter_click[ORIGINAL] / counter_show[ORIGINAL]
    except ZeroDivisionError as eror:
        test_indicator = 0
        original_indicator = 0

    return render_to_response('stats.html', context={
        'test_conversion': test_indicator,
        'original_conversion': original_indicator,
    })
