from django.shortcuts import render, redirect
from django.core.paginator import Paginator


class ObjectsListMixin():
    model = None
    template = None

    def get(self, request):
        paginator = Paginator(self.model.objects.all(), 2)
        page_obj = paginator.page(request.GET.get('page'))

        context = {
            'title': f'{self.model.__name__}',
            'page_obj': page_obj,
            'paginator': paginator

        }
        return render(request, self.template, context)


class CreatorObjectsMixin():

    model = None
    template = None
    form = None

    def get(self, request):
        form = self.form()
        context = {'form': form}
        return render(request, self.template, context)

    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            form.save()
            return redirect(f'{self.model.__name__.lower()}-list')
        context = {'form': form}
        return render(request, self.template, context)


class UpdateObjectsMixin():

    model = None
    template = None
    form = None

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(instance=obj)
        context = {
            'form': form,
            'object': obj,
        }
        return render(request, self.template, context)

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        form = self.form(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(f'{self.model.__name__.lower()}-list')

        context = {
            'form': form,
            'object': obj,
        }
        return render(request, self.template, context)


class DeleteObjectsMixin():
    model = None
    template = None

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        return render(request, self.template, {'object': obj})

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        obj.delete()
        return redirect(f'{self.template.__name__.lower()}-list')




