from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)


    def __str__(self):
        return f"{self.nickname}"


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.time_now = time_now
        self.adult_mode = adult_mode
        self.title = str(title)
        self.duration = int(duration)


    def __str__(self):
        return f"{self.title}"


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    def __str__(self):
        if self.current_user != None:
            return f"{self.current_user.nickname}"


    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname:
                if user.password == hash(password):
                    self.current_user = user
                    return


    def register(self, nickname, password, age):
        if not any(user.nickname == nickname for user in self.users):
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.log_in(nickname, password)
        else:
            print(f"Пользователь {nickname} уже существует")


    def log_out(self):
        self.current_user = None


    def add(self, *videos):
        for video in videos:
            if not any(vid.title == video.title for vid in self.videos):
                self.videos.append(video)


    def get_videos(self, keyword):
        matching_list = []
        keyword = str(keyword)
        for video in self.videos:
            if keyword.lower() in video.title.lower():
                matching_list.append(video)
        return [str(video) for video in matching_list]


    def watch_video(self, v_title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video in self.videos:
                if v_title == video.title:
                    if self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        while video.time_now < video.duration:
                            #sleep(1)
                            video.time_now += 1
                            print(video.time_now, end=' ')
                        print("Конец видео")



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')