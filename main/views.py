from flask import Blueprint, render_template, request

from dao.dao import PostsDAO

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

posts = PostsDAO('./data/posts.json', './data/comments.json')


@main_blueprint.route('/')
def index_page():
    all_posts = posts.load_posts()
    return render_template('index.html', posts=all_posts)


@main_blueprint.route('/posts/<int:post_id>')
def post_page(post_id):
    post = posts.get_post_by_pk(post_id)
    comments = posts.get_comments_by_post_id(post_id)
    return render_template('post.html', post=post, comments=comments)


@main_blueprint.route('/search', methods=['GET'])
def search_page():
    query = request.args.get('s')
    found_posts = posts.search_for_posts(query)
    return render_template('search.html',  posts=found_posts)

@main_blueprint.route('/users/<username>', methods=['GET'])
def user_page(username):
    user_posts = posts.get_posts_by_user(username)
    return render_template('user-feed.html', posts=user_posts, username=username)


@main_blueprint.errorhandler(404)
def not_found_error(error):
    return f'Страницы не существует, ошибка {error}'


@main_blueprint.errorhandler(500)
def server_error(error):
    return f'Ошибка сервера {error}'
