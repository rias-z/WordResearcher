from django.views import generic
from django import forms
# from django.shortcuts import render
# from django.http import HttpResponseRedirect
from .models import Element, Category
from itertools import chain


# Form
class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ["title", "content", "category", "slide_num"]


# View
class TopView(generic.TemplateView):
    template_name = "top.html"

    def get_context_data(self, **kwargs):
        context = super(TopView, self).get_context_data(**kwargs)
        context["loop_time"] = range(1, 8)
        return context


class SearchView(generic.TemplateView):
    template_name = "result.html"

    def post(self, request, *args, **kwargs):
        search_word = self.request.POST["search_word"]
        mode = self.request.POST["mode"]

        context = self.get_context_data()
        if mode == "all":
            elements_title = Element.objects.filter(title__contains=search_word)
            elements_content = Element.objects.filter(content__contains=search_word)
            elements_category = Element.objects.filter(category__name__in=[search_word])
            query_result = sorted(set(chain(elements_title, elements_content, elements_category)),
                                  key=lambda instance: instance.id)
        elif mode == "title_only":
            query_result = Element.objects.filter(title__contains=search_word)
        elif mode == "category_search":
            query_result = Element.objects.filter(category__name__in=[search_word])
        elif mode == "slide_num_search":
            query_result = Element.objects.filter(slide_num=search_word)
        else:
            pass

        context["search_word"] = search_word
        context["query_result"] = query_result
        return super(SearchView, self).render_to_response(context)


class DetailView(generic.DetailView):
    template_name = "detail.html"
    model = Element
    form_class = ElementForm

    def get_queryset(self):
        self.queryset = Element.objects.all()
        return super(DetailView, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["element"] = self.get_object()
        context["category"] = self.get_object().category.all()
        return context
