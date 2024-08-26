from django import forms
from .models import ArticleCategory, ArticleTag, Article, ArticleComment
from django_summernote.widgets import SummernoteWidget


class ArticleCategoryForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the article category name.", label="Name")
    slug = forms.SlugField(required=False)

    class Meta:
        model = ArticleCategory
        fields = "__all__"


class ArticleTagForm(forms.ModelForm):
    name = forms.CharField(help_text="Provide the article tag name.", label="Name")
    slug = forms.SlugField(required=False)

    class Meta:
        model = ArticleTag
        fields = "__all__"


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=200, help_text="Provide the article title.", label="Title")
    image = forms.ImageField(help_text="Upload an image of the article.", label="Image", required=True)
    description = forms.CharField(max_length=100000, help_text="Provide the article description.", label="Description",
                                  widget=SummernoteWidget())
    slug = forms.SlugField(required=False)

    class Meta:
        model = Article
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)

        self.fields["user"].help_text = "Select the author of the article."
        self.fields["user"].label = "Author"

        self.fields["article_category"].help_text = "Provide the category of the article."
        self.fields["article_category"].help_text = "Category"

        self.fields["article_tags"].help_text = "Provide the tag of the article."
        self.fields["article_tags"].label = "Tag"
        self.fields["article_tags"].required = False


class ArticleCommentForm(forms.ModelForm):
    fullname = forms.CharField(help_text="Provide the full name of the comment author.", label="Guest Author",
                               required=False)
    email = forms.EmailField(help_text="Provide the e-mail address of the comment author.", label="E-mail Address",
                             required=False)
    comment = forms.CharField(help_text="Provide the comment.", label="Comment Content")
    is_active = forms.BooleanField(help_text="Indicate whether the comment is active.", required=False)

    class Meta:
        model = ArticleComment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ArticleCommentForm, self).__init__(*args, **kwargs)

        self.fields["user"].help_text = "Select the author of the comment."
        self.fields["user"].label = "Logged-In Author"
        self.fields["user"].required = False

        self.fields["article"].help_text = "Select the article to comment on."
        self.fields["article"].label = "Article"
