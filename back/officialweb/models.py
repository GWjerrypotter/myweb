from django.db import models


class DocType(models.Model):
    doc_type = models.CharField(max_length=16, verbose_name='文档类型')
    en_type = models.CharField(max_length=16, verbose_name='英文名', default='0')
    type_remark = models.TextField(max_length=128, verbose_name='文档类型备注', null=True, blank=True)

    def __str__(self):
        return self.doc_type

    class Meta(object):
        verbose_name = '文档类型管理'
        verbose_name_plural = verbose_name


class Docs(models.Model):
    doc_type = models.ForeignKey(DocType, on_delete=models.CASCADE, verbose_name='文档类型')
    doc_title = models.CharField(max_length=32, verbose_name='文档标题')
    author = models.ForeignKey('users.Users', on_delete=models.CASCADE, verbose_name='作者')
    doc_content = models.TextField(max_length=None, verbose_name='文档内容')
    doc_file = models.FileField(upload_to='uploads/', verbose_name='附件', null=True, blank=True)
    publish_time = models.DateTimeField(auto_now=True, verbose_name='发布时间')
    clicks = models.PositiveIntegerField(verbose_name='点击量', default=0)
    doc_remark = models.CharField(max_length=128, verbose_name='文档备注', null=True, blank=True)

    def __str__(self):
        return self.doc_title

    class Meta(object):
        verbose_name = '文档管理'
        verbose_name_plural = verbose_name
