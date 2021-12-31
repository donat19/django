from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import loader
from .forms import ExampleForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


def home(request):
    a = loader.render_to_string('task_2.html', request=request)
    return HttpResponse(a)


data = {'lukepage': 'Люк Скайуокер — один из главных персонажей вселенной «Звёздных войн», джедай, сын сенатора '
                    'с Набу Падме Амидалы Наберри и рыцаря-джедая Энакина Скайуокера',
        'hanpage': 'Хан. Соло — пилот космического корабля «Тысячелетний сокол», его бортмехаником и вторым '
                   'пилотом является вуки по имени Чубакка.',
        'leipage': 'Лея Органа — дочь рыцаря-джедая Энакина Скайуокера и сенатора Падме Амидалы Наберри.'}


def postpage(request, name):
    return render(request, 'task_2_2.html', {'text': data[name]})


def dz1(request):
    context = {'lets_do_it': [
        {'priority': 100, 'task': 'Составить список дел'},
        {'priority': 150, 'task': 'Изучать Django'},
        {'priority': 1, 'task': 'Подумать о смысле жизни'}
    ]}
    test_template = loader.render_to_string('dz1.html',
                                            context=context)
    return HttpResponse(test_template)


class Dz(TemplateView):
    template_name = "Dz.html"

    def get_context_data(self, **kwargs):
        return {'latest_question_list': [{'id': 1,
                                          'question_text': 'В чем смысл жизни?'},
                                         {'id': 2,
                                          'question_text': 'Что первично, дух или материя?'},
                                         {'id': 3,
                                          'question_text': 'Существует ли свобода воли?'}]}


def postpage(request, number):
    if number == 1:
        return HttpResponse(
            "Кто-то или что-то на славу потрудилось, "
            "придумав нас настолько непохожими друг на друга,"
            " но в одном это что-то явно загналось несильно,"
            " а именно в человеческой необходимости стремиться"
            " к чему-либо. Да, каждый человек уникален,"
            " но не существует ни одной жизни, в которой не"
            " было бы мечт, желаний, и целей, ведь все мы куда-то"
            " движемся в нашем существовании, нам важно чего-то достичь,"
            " никто из нас не хочет прожить зря.")
    elif number == 2:
        return HttpResponse(
            "Обычно проблематизируется в форме вопроса:"
            " «Что первично, дух или материя?»."
            " Марксизм выделяет два основных варианта"
            " решения основного вопроса философии:"
            " материализм, при котором материя обладает"
            " преимуществом по отношению к сознанию,"
            " и идеализм, при котором идея первична к материи.")
    elif number == 3:
        return HttpResponse(
            "В наше время любят говорить: "
            "свободы воли не существует (речь идет о"
            " свободе человека как мыслящего и действующего"
            " существа). В современной философии подобные идеи можно"
            " подвести под рубрику «физикализм». В простейшем"
            " обобщении физикализм утверждает, что представление о "
            "свободе воли (или, иначе, возможности выбора) есть чистейшая"
            " иллюзия, мы функционируем по программе, «встроенной» в нас"
            " природой, и свободы у нас не больше, чем у растения или"
            " животного.")
    else:
        return HttpResponse("Другой вопрос")


class ExampleFormView(FormView):
    form_class = ExampleForm
    template_name = "model_form_page.html"
    success_url = reverse_lazy("example_form_success")


def example_success(request):
    return HttpResponse('Спасибо за отзыв!')


def my_form (request):
    print(request.POST)
    form = ExampleForm(request.POST or None, request.FILES or None)

    return render(request, 'model_form_page.html', context={'form':  form})
