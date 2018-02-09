from myapp.models import Dreamreal, Online
dr1 = Dreamreal()
dr1.website = 'company1.com'
dr1.name = 'company1'
dr1.mail = 'contact@company1'
dr1.phonenumber = '12345'
dr1.save()
dr2 = Dreamreal()
dr1.website = 'company2.com'
dr2.website = 'company2.com'
dr2.name = 'company2'
dr2.mail = 'contact@company2'
dr2.phonenumber = '56789'
dr2.save()