from django.db import models
from django.contrib.auth.models import User


# verbose_name = admin 에 내가 지정해준 이름으로 나옴
# DateTimeField = 날짜와 시간정보 표현
# CharField = 문자열을 담을수있는 필드
# dttm = 데이트 타임의 약자
class Partner(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name='사용자명')
    loginPW = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    loginID = models.CharField(max_length=20,
                            verbose_name='학번')
    usernumber = models.CharField(max_length=64,
                                    verbose_name='전화번호1')
    usernumber2 = models.CharField(max_length=64,
                                    verbose_name='전화번호2')
    class Meta:
        db_table = 'DGFOOD_partner'
        verbose_name_plural = '동국푸드 유저'



class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=50,
        verbose_name="업체 이름",
    )
    contact = models.CharField(
        max_length=50,
        verbose_name="연락처",
    )
    address = models.CharField(
        max_length=200,
        verbose_name="주소",
    )
    description = models.TextField(
        verbose_name="상세 소개",
    )
    class Meta:
        db_table = "DGFOOD_store"
        verbose_name_plural = '동국푸드 업체'

        
class Menu(models.Model):
    store = models.ForeignKey(Store,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        verbose_name = "메뉴 이미지"
    )
    name = models.CharField(
        max_length=50,
        verbose_name = "메뉴 이름"
    )
    price = models.PositiveIntegerField(
        verbose_name = "가격"
    )

    class Meta:
        db_table = 'DGFOOD_menu'
        verbose_name_plural = '동국푸드 메뉴'

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     nickname = models.TextField(max_length=10)
    # registered_dttm = models.DateTimeField(auto_now_add=True,
    #                                         verbose_name='등록시간')

    def __str__(self):# 이거 유저네임을 보여주게함 프로젝트 오브젝트 말고
        return self.username

# db에 테이블 명 지정해고 싶을때 지정이유는 기본적으로 생성되는 앱있는데
# 그앱들과 구분지어 줄라고
