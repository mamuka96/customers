from django.shortcuts import render, redirect

class ObjectsListMixin():
    model = None
    template = None

    def get(self, request):
        context = {
            'title': f'{self.model.__name__}',
            'objects': self.model.objects.all(),
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