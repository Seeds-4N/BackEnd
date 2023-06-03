from django.db import models
from django.urls import reverse
from accounts.models import User


# class BookmarkManager(models.Manager):
#     pass


# 북마크
class Bookmark(models.Model):
    name = models.CharField(max_length=50, verbose_name="북마크")
    description = models.CharField(max_length=100, null=True, blank=True, verbose_name="북마크 설명")

    # objects = BookmarkManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'forum_bookmark'
        verbose_name = '북마크'
        verbose_name_plural = '북마크'


# default_bookmark = Bookmark.objects.create(name='기본 북마크')


# 폴더
class Folder(models.Model):
    name = models.CharField(max_length=20, verbose_name="폴더")
    description = models.CharField(max_length=100, null=True, blank=True, verbose_name="폴더 설명")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'forum_folder'
        verbose_name = '폴더'
        verbose_name_plural = '폴더'


# 글(제목, 작성일, 내용, 북마크, 폴더)
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='작성일')    # 작성일자동입력
    updateDate = models.DateTimeField(auto_now_add=True, verbose_name='수정일')    # 수정일자동입력
    # 북마크와 글은 1:N 관계이므로 ForeignKey 사용
    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE, verbose_name='북마크')
    # 폴더와 글은 다대다 관계이므로 ManyToManyField 사용 (M2M에선 on_delete 옵션을 사용하지 않는다고 함)
    # 폴더를 설정하지 않을 수 있고 폴더가 삭제되더라도 포스트는 삭제되지 않음
    folder = models.ManyToManyField(Folder, blank=True, verbose_name='폴더')
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.pk)])

    class Meta:
        db_table = 'forum_post'
        verbose_name = '게시물'
        verbose_name_plural = '게시물'
