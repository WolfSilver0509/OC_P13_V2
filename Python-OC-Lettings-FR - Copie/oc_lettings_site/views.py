from django.shortcuts import render
# from models import  Profile

# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis
# leo consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis,
# sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum
# lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis
# enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.


def index(request):
    return render(request, 'index.html')

# # Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# # Sed non placerat massa. Integer est nunc, pulvinar a
# # tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci
# # luctus et ultrices posuere cubilia curae; Cras eget scelerisque
#
#
# def profiles_index(request):
#     profiles_list = Profile.objects.all()
#     context = {'profiles_list': profiles_list}
#     return render(request, 'index.html', context)
#
# # Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# # laoreet neque quis, pellentesque dui. Nullam facilisis pharetra
# # vulputate. Sed tincidunt, dolor id facilisis fringilla,
# # eros leo tristique lacus,
# # it. Nam aliquam dignissim congue. Pellentesque
# # habitant morbi tristique senectus et netus et males
#
#
# def profile(request, username):
#     profile = Profile.objects.get(user__username=username)
#     context = {'profile': profile}
#     return render(request, 'profile.html', context)