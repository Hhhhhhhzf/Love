from django.db import models
from users.models import MyUser
# Create your models here.


# 留言表
class Message(models.Model):
    # TODO 和谐脏话、添加emoji表情
    text = models.TextField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=True)
    is_legal = models.BooleanField(default=True)
    bak = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.text[:50] + "..."


# 留言赞表
class MessageLike(models.Model):
    like_user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    is_viewed = models.BooleanField(default=False)

    is_valid = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    bak = models.CharField(max_length=100)


# 留言评论表
class MessageComment(models.Model):
    from_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='from_user', default="")
    to_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='to_user', default="")
    father_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='father_comment_id', default="")
    earliest_sub_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_comment_id', default="")
    sub_comment_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    content = models.TextField()
    is_viewed = models.BooleanField(default=True)
    is_valid = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    bak = models.CharField(max_length=100)


# 留言评论赞表
class MessageCommentLike(models.Model):
    like_user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment = models.ForeignKey(MessageComment, on_delete=models.CASCADE)
    is_viewed = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    bak = models.CharField(max_length=100)
