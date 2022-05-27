import logging

from flask import Blueprint, render_template, request, abort
from app.posts.dao.posts_dao import PostsDAO
from app.posts.dao.comments_dao import CommentsDAO

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
posts_dao = PostsDAO("data/posts.json")
comments_dao = CommentsDAO("data/comments.json")

logger = logging.getLogger("basic")

@posts_blueprint.route('/')
def posts_all():
    logger.debug("Запрошены все посты")
    try:
        posts = posts_dao.get_all()
        return render_template("index.html", posts = posts)

    except:
        return "Что-то пошло не так"

@posts_blueprint.route('/posts/<int:post_pk>')
def posts_one(post_pk):
    logger.debug(f"Запрошен пост {post_pk}")
    try:
        post = posts_dao.get_by_pk(post_pk)
        comments = comments_dao.get_by_post_pk(post_pk)
    except:
        return "Произошла ошибка при получении данных постов"
    else:
        if post is None:
            abort(404)
        number_of_comments = len(comments)
        return render_template("post.html", post=post, comments=comments, number_of_comments=number_of_comments)

@posts_blueprint.route('/search/')
def posts_search():

    query = request.args.get("s", None)
    posts = posts_dao.search(query)
    number_of_posts = len(posts)

    return render_template("search.html", query=query, posts=posts, number_of_posts=number_of_posts)

@posts_blueprint.route('/users/<username>')
def posts_by_user(username):

    posts = posts_dao.get_by_user(username)
    number_of_posts = len(posts)

    return render_template("user-feed.html", posts=posts, number_of_posts=number_of_posts)

@posts_blueprint.errorhandler(404)
def post_error(e):
    return "Такой пост не найден", 404