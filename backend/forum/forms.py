from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):    # 보고 따라하긴 했는데 아직 이해 부족
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })

    class Meta:
        model = Post
        fields = ['title', 'content','bookmark', 'folder']
