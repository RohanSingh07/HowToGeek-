from django.shortcuts import render,redirect
from .models import Blog,Comments,Contacts
from .forms import NewForm
# Create your views here.
def HomeView(request):

    blogs = Blog.objects.all()[0:2]
    return render(request,'index.html',{

        'blogs':blogs
    })


def ContactView(request):
    if request.method =="GET":
        return render(request,'contact.html',{})
    else:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contacts(
            Name = name,
            email = email,
            subject = subject,
            message = message
        )
        contact.save()
        return redirect("Blogs:HomeView")

def BlogView(request,slug):
    if request.method =='GET':
        blog = Blog.objects.filter(slug=slug)

        if blog.exists():
            blog = blog[0]
        return render(request,'blog.html',{
            'blog':blog
        })
    else:
        blog = Blog.objects.filter(slug=slug)[0]
        comment = request.POST['comment']
        name = request.POST['name']
        com = Comments(
            Comment = comment,
            Name = name
        )
        com.save()
        blog.coments.add(com)
        blog.save()
        return render(request, 'blog.html', {
            'blog': blog
        })



def AboutView(request):
    blogs = Blog.objects.all()


    return render(request,'about.html',{
        'blogs':blogs
    })

def AddBlog(request):
    if request.method == "GET":
        form = NewForm()
        return render(request,'AddBlog.html',{
            'form':form
        })
    else:
        form = NewForm(request.POST ,request.FILES)
        if form.is_valid():
            Name = form.cleaned_data.get('Name')
            Background_Image = form.cleaned_data.get('Background_Image')
            Subheading1 = form.cleaned_data.get('Subheading1')
            Image1 = form.files.get('Image1')
            Paragraph1 = form.cleaned_data.get('Paragraph1')
            Subheading2 = form.cleaned_data.get('Subheading2')
            Image2 = form.files.get('Image2')
            Paragraph2 = form.cleaned_data.get('Paragraph2')
            Subheading3 = form.cleaned_data.get('Subheading3')
            Image3 = form.files.get('Image3')
            Paragraph3 = form.cleaned_data.get('Paragraph3')
            video = form.files.get('Video')
            slug = form.cleaned_data.get('slug')
            NewBlog = Blog(
                Name = Name,
                Background_Image = Background_Image,
                Subheading1 = Subheading1,
                Image1 = Image1,
                Paragraph1 = Paragraph1,
                Subheading2 = Subheading2,
                Image2 = Image2,
                Paragraph2 = Paragraph2,
                Subheading3 = Subheading3,
                Image3 = Image3,
                Paragraph3 = Paragraph3,
                Video = video,
                slug = slug

            )
            NewBlog.save()
        else:
            pass
        return redirect("Blogs:AboutView")

def EditBlog(request,slug):
    blog = Blog.objects.get(slug=slug)
    if request.method == 'GET':

        form = NewForm(instance=blog)

        return render(request,'EditBlog.html',{
            'form':form
        })
    else:
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            Name = form.cleaned_data.get('Name')
            Background_Image = form.cleaned_data.get('Background_Image')
            Subheading1 = form.cleaned_data.get('Subheading1')
            Image1 = form.files.get('Image1')
            Paragraph1 = form.cleaned_data.get('Paragraph1')
            Subheading2 = form.cleaned_data.get('Subheading2')
            Image2 = form.files.get('Image2')
            Paragraph2 = form.cleaned_data.get('Paragraph2')
            Subheading3 = form.cleaned_data.get('Subheading3')
            Image3 = form.files.get('Image3')
            Paragraph3 = form.cleaned_data.get('Paragraph3')
            video = form.files.get('Video')
            slug = form.cleaned_data.get('slug')

            blog.Name=Name
            blog.Background_Image=Background_Image
            blog.Subheading1=Subheading1
            blog.Image1=Image1
            blog.Paragraph1=Paragraph1
            blog.Subheading2=Subheading2
            blog.Image2=Image2
            blog.Paragraph2=Paragraph2
            blog.Subheading3=Subheading3
            blog.Image3=Image3
            blog.Paragraph3=Paragraph3
            blog.Video=video
            blog.slug=slug


            blog.save()
            return redirect('Blogs:AboutView')
