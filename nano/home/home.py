from flask import Blueprint, render_template

home_bp = Blueprint(name="home_bp", import_name=__name__, url_prefix="/")

featured_posts = [
    {
        "title": "Understanding Quantum Computing in Simple Terms",
        "description": "A brief introduction to quantum computing and its potential impact.",
        "image": "https://via.placeholder.com/350x250",
        "link": "#",
    },
    {
        "title": "The Future of Artificial Intelligence",
        "description": "Exploring the next big breakthroughs in AI technology.",
        "image": "https://via.placeholder.com/350x250",
        "link": "#",
    },
    {
        "title": "How Minimalism Can Improve Your Life",
        "description": "Discover the power of living with less and its benefits for your mental health.",
        "image": "https://via.placeholder.com/350x250",
        "link": "#",
    },
]


@home_bp.route(rule="/")
def home():
    return render_template(
        template_name_or_list="landing_page.html", featured_posts=featured_posts
    )
