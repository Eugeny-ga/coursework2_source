import logging
from flask import Blueprint, jsonify
from dao.dao import PostsDAO

logger = logging.getLogger("api_logger")
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler = logging.FileHandler("../logs/api.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


api_blueprint = Blueprint('api_blueprint', __name__)
posts = PostsDAO('./data/posts.json', './data/comments.json')


@api_blueprint.route('/api/posts/', methods=["GET"])
def get_all_posts():
    all_posts = posts.load_posts_json()
    logger.info('Posts requests')
    return jsonify(all_posts)


@api_blueprint.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = posts.get_post_by_pk_json(post_id)
    logger.info(f'Post {post_id} request')
    return jsonify(post)
