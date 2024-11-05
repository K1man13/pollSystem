from django.utils import timezone  # Make sure you have this import
from django.views import generic
from django.shortcuts import render
from.models import Question
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'  # Ensure you have this template created

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choices'] = self.object.choice_set.all()  # Add choices to context
        return context