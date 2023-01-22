import json

from dao.post import Post


class PostsDAO:
    def __init__(self, posts_path, comments_path):
        self.posts_path = posts_path
        self.comments_path = comments_path

    def load_posts(self):
        """Возвращает посты в виде объектов класса"""
        with open(self.posts_path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
            all_posts = []
            for post in posts:
                all_posts.append(Post(
                    post["poster_name"],
                    post["poster_avatar"],
                    post["pic"],
                    post["content"],
                    post["views_count"],
                    post["likes_count"],
                    post["pk"]
                ))
            return all_posts

    def load_posts_json(self):
        """Возвращает посты в виде словаря """
        with open(self.posts_path, 'r', encoding='utf-8') as file:
            posts = json.load(file)
            return posts


    def get_all_posts(self):
        return self.load_posts()


    def get_posts_by_user(self, username):
        """Возвращает посты юзера user_name,
        либо ValueError, если пользователя нет,
        либо пустой список, если нет постов"""

        posts = self.load_posts()
        user_posts = []
        for post in posts:
            if post.poster_name.lower() == username.lower():
                user_posts.append(post)
        return user_posts

    def get_post_by_pk(self, pk):
        """Возвращает один пост по его pk как объект класса"""
        posts = self.load_posts()
        for post in posts:
            if post.pk == pk:
                return post


    def get_post_by_pk_json(self, pk):
        """Возвращает один пост по его pk в виде словаря"""
        posts = self.load_posts_json()
        for post in posts:
            if post['pk'] == pk:
                return post
        return



    def search_for_posts(self, query):
        """Возвращает список постов по ключевому слову"""
        posts = self.load_posts()
        found_posts = []
        for post in posts:
            if query in post.content.lower():
                found_posts.append(post)
        return found_posts


    def get_comments_all(self):
        """Возвращает комментарии"""
        with open(self.comments_path, 'r', encoding='utf-8') as file:
            comments = json.load(file)
            return comments


    def get_comments_by_post_id(self, post_id):
        """Возвращает комментарии определенного поста.
        ValueError, если поста нет, либо пустой список, если нет комментов"""
        comments = self.get_comments_all()

        post_comments = []
        for comment in comments:
            if comment['post_id'] == post_id:
                post_comments.append(comment)
        return post_comments
