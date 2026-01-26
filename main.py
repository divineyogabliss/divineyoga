from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import yaml
import markdown

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

BLOGS_DIR = "blogs"

# =========================
# CATEGORY META
# =========================

CATEGORY_DATA = {
    "mudras": {
        "title": "Mudras",
        "image": "/static/bg/mudras.png",
        "description": "Learn powerful hand gestures that balance energy, improve focus, and promote healing.",
    },
    "pranayamas": {
        "title": "Pranayamas",
        "image": "/static/bg/pranayamas.png",
        "description": "Breathing techniques to calm the mind, improve lung capacity, and boost vitality.",
    },
    "asanas": {
        "title": "Asanas",
        "image": "/static/bg/asanas.png",
        "description": "Yoga postures that build strength, flexibility, balance, and body awareness.",
    },
    "meditation": {
        "title": "Meditation",
        "image": "/static/bg/meditation.png",
        "description": "Mindfulness practices to reduce stress, enhance clarity, and find inner peace.",
    },
    "chakras": {
        "title": "Chakras",
        "image": "/static/bg/chakras.png",
        "description": "Understand and balance the body’s energy centers through deep awareness practices.",
    },
    "bandhas": {
        "title": "Bandhas",
        "image": "/static/bg/bandas.png",
        "description": "Learn internal energy locks that activate prana flow and inner strength.",
    },
}


# -----------------------------
# CATEGORY → GOOGLE FORM ENROLL LINKS
# -----------------------------
form_url="https://docs.google.com/forms/d/e/1FAIpQLSd11WJ4JyL2Di0tAsWY4ryfUtIUlwsaC_7DqfWcCH18xbBAYA/viewform?usp=dialog"
CATEGORY_FORMS = {
    "mudras": {"course_name": "Mudras Course", "form_url": form_url},
    "pranayamas": {"course_name": "Pranayama Course", "form_url":form_url},
    "asanas": {"course_name": "Asanas Course", "form_url": form_url},
    "meditation": {"course_name": "Meditation Program", "form_url": form_url},
    "chakras": {"course_name": "Chakra Healing Workshop", "form_url": form_url},
    "bandhas": {"course_name": "Bandhas Training", "form_url": form_url},
}

CATEGORY_COURSES =[
    {
        "id": "asanas_7",
        "title": "7-Day Asanas Course",
        "price": 389,
        "duration": "7 Days",
        "category": "asanas",
        "features": ["Live Yoga Class", "PDF Guide"],
    },
    {
        "id": "meditation_21",
        "title": "21-Day Meditation Program",
        "price": 199,
        "duration": "21 Days",
        "category": "meditation",
        "tag": "Recommended",
        "features": ["Live Class", "Meditation Audios", "Progress Tracker"],
    },
    {
        "id": "mudras_3",
        "title": "3-Day Mudras Workshop",
        "price": 199,
        "duration": "3 Days",
        "category": "mudras",
        "features": ["Zoom Class", "Practice PDF"],
    },
]
# -----------------------------
# COURSE CATALOG (MULTIPLE ASANAS VARIANTS)
# -----------------------------
COURSES = [

    # ========= ASANAS PROGRAMS =========
    {
        "slug": "asanas-3-days",
        "title": "Asanas Course — 3 Days",
        "price": 199,
        "duration": "3 Days",
        "features": ["Beginner intro program", "Light flexibility drills", "Posture awareness"],
        "form_url": form_url
    },
    {
        "slug": "asanas-5-days",
        "title": "Asanas Course — 5 Days",
        "price": 299,
        "duration": "5 Days",
        "features": ["Core strength focus", "Stretch & relax routine", "Guided warmup sets"],
        "form_url": form_url
    },
    {
        "slug": "asanas-11-days",
        "title": "Asanas Course — 11 Days",
        "price": 499,
        "duration": "11 Days",
        "features": ["Daily class", "Joint mobility work", "Beginner to intermediate flow"],
        "form_url": form_url
    },
    {
        "slug": "asanas-21-days",
        "title": "Asanas Course — 21 Days",
        "price": 799,
        "duration": "21 Days",
        "features": ["Habit building program", "Strength + flexibility", "Progress tracking"],
        "form_url": form_url
    },
    {
        "slug": "asanas-30-days",
        "title": "Asanas Course — 30 Days",
        "price": 1999,
        "duration": "30 Days",
        "features": ["Daily flexibility training", "Back & hip mobility", "Personal guidance"],
        "form_url": form_url
    },
    {
        "slug": "asanas-45-days",
        "title": "Asanas Course — 45 Days",
        "price": 2999,
        "duration": "45 Days",
        "features": ["Strengthening routine", "Endurance & stamina", "Deep stretch therapy"],
        "form_url": form_url
    },
    {
        "slug": "asanas-60-days",
        "title": "Asanas Course — 60 Days",
        "price": 3999,
        "duration": "60 Days",
        "features": ["Full body toning", "Breath + posture sync", "Deep flexibility"],
        "form_url": form_url
    },
    {
        "slug": "asanas-120-days",
        "title": "Asanas Course — 120 Days",
        "price": 5999,
        "duration": "120 Days",
        "features": ["Lifestyle alignment", "Body transformation", "Discipline building"],
        "form_url": form_url
    },
    {
        "slug": "asanas-6-months",
        "title": "Asanas Course — 6 Months",
        "price": 6999,
        "duration": "6 Months",
        "features": ["Long-term posture correction", "Strength & conditioning", "Holistic flexibility"],
        "form_url": form_url
    },
    {
        "slug": "asanas-1-year",
        "title": "Asanas Course — 1 Year",
        "price": 15999,
        "duration": "1 Year",
        "features": ["Deep transformative journey", "Discipline & consistency", "Advanced flexibility"],
        "form_url": form_url
    },

    # ========= EXISTING MEDITATION COURSE =========
    {
        "slug": "mudras",
        "title": "3-Day Mudras Course",
        "price": 199,
        "duration": "3 Days Mudras",
        "features": ["Live class", "Progress tracker"],
        "form_url": form_url
    },
    {
        "slug": "pranayamas",
        "title": "3-Day Pranayamas Course",
        "price": 199,
        "duration": "3 Days Pranayamas",
        "features": ["Live class", "Progress tracker"],
        "form_url": form_url
    },
    {
        "slug": "Energy Anatomy",
        "title": "3-Day Energy Anatomy Course",
        "price": 199,
        "duration": "3 Days Energy Anatomy",
        "features": ["Live class", "Progress tracker"],
        "form_url": form_url
    },
    {
        "slug": "Relaxation Techniques",
        "title": "2-Day Meditation Course",
        "price": 199,
        "duration": "2 Days Mediation",
        "features": ["Live class", "Meditation audios", "Progress tracker"],
        "form_url": form_url
    },
]

CHANTS_DIR = "chants"
import markdown

def load_blogs_for_category(category: str):
    blogs = []
    path = os.path.join(BLOGS_DIR, category)

    if not os.path.exists(path):
        return blogs

    for filename in sorted(os.listdir(path)):
        if not filename.endswith(".md"):
            continue

        with open(os.path.join(path, filename), encoding="utf-8") as f:
            content = f.read()

        try:
            meta, body = content.split("\n\n", 1)
            meta_yaml = yaml.safe_load(meta)
        except:
            continue

        blogs.append({
            "title": meta_yaml.get("title", "Untitled Blog"),
            "summary": meta_yaml.get("summary", ""),
            "slug": filename.replace(".md", ""),
            "category": category,
        })

    return blogs





def load_chants():
    chants = []

    for category in os.listdir(CHANTS_DIR):

        category_path = os.path.join(CHANTS_DIR, category)

        if not os.path.isdir(category_path):
            continue

        for filename in os.listdir(category_path):

            if not filename.endswith(".md"):
                continue

            filepath = os.path.join(category_path, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            try:
                meta, body = content.split("\n\n", 1)
                meta_yaml = yaml.safe_load(meta)
            except Exception:
                continue

            chants.append({
                "title": meta_yaml.get("title", "Untitled Chant"),
                "deity": meta_yaml.get("deity", ""),
                "origin": meta_yaml.get("origin", ""),
                "language": meta_yaml.get("language", ""),
                "benefits": meta_yaml.get("benefits", ""),
                "duration": meta_yaml.get("duration", ""),
                "slug": filename.replace(".md", ""),
                "category": category,
            })

    return chants



def load_chant_by_slug(slug: str):
    for category in os.listdir(CHANTS_DIR):

        filepath = os.path.join(CHANTS_DIR, category, f"{slug}.md")

        if not os.path.exists(filepath):
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        try:
            meta, body = content.split("\n\n", 1)
            meta_yaml = yaml.safe_load(meta)
        except Exception:
            return None

        html_body = markdown.markdown(body, extensions=["extra"])

        return {
            "title": meta_yaml.get("title", "Untitled Chant"),
            "deity": meta_yaml.get("deity", ""),
            "origin": meta_yaml.get("origin", ""),
            "language": meta_yaml.get("language", ""),
            "benefits": meta_yaml.get("benefits", ""),
            "duration": meta_yaml.get("duration", ""),
            "category": category,
            "content": html_body,
        }

    return None

def load_blog_by_slug(slug: str):
    for category in CATEGORY_DATA.keys():
        path = os.path.join(BLOGS_DIR, category, f"{slug}.md")

        if not os.path.exists(path):
            continue

        with open(path, encoding="utf-8") as f:
            content = f.read()

        try:
            meta, body = content.split("\n\n", 1)
            meta_yaml = yaml.safe_load(meta)
        except:
            return None

        return {
            "title": meta_yaml.get("title", "Untitled Blog"),
            "date": meta_yaml.get("date", ""),
            "category": category,
            "content": markdown.markdown(body, extensions=["extra"]),
        }

    return None

def get_course(slug):
    return next((c for c in COURSES if c["slug"] == slug), None)

def load_all_blogs():
    all_items = []
    for c in CATEGORY_DATA.keys():
        all_items += load_blogs_for_category(c)
    return all_items


# =========================
# ROUTES
# =========================

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "courses": COURSES,
            "categories": CATEGORY_DATA,
        }
    )


@app.get("/category/{category}")
def category_page(category: str, request: Request):
    category = category.lower()

    if category not in CATEGORY_DATA:
        return {"error": "Category not found"}

    blogs = load_blogs_for_category(category)
    enroll = CATEGORY_FORMS.get(category)

    related_courses = [c for c in CATEGORY_COURSES if c["category"] == category]

    return templates.TemplateResponse(
        "category.html",
        {
            "request": request,
            **CATEGORY_DATA[category],
            "blogs": blogs,
            "enroll": enroll,
            "courses": related_courses,
        }
    )


@app.get("/blog/{slug}")
def blog_page(slug: str, request: Request):
    blog = load_blog_by_slug(slug)

    if not blog:
        return {"error": "Blog not found"}

    enroll = CATEGORY_FORMS.get(blog["category"])

    return templates.TemplateResponse(
        "blog.html",
        {
            "request": request,
            "blog": blog,
            "CATEGORY_DATA": CATEGORY_DATA,
            "enroll": enroll,
        }
    )


@app.get("/courses")
def courses(request: Request):
    return templates.TemplateResponse("courses.html", {
        "request": request,
        "courses": COURSES
    })


@app.get("/course/{slug}")
def course_detail(slug: str, request: Request):
    course = get_course(slug)
    if not course:
        return {"error": "Course not found"}
    return templates.TemplateResponse("course_detail.html", {
        "request": request,
        "course": course
    })

@app.get("/chants")
def chant_list(request: Request):
    chants = load_chants()
    return templates.TemplateResponse("chants.html", {
        "request": request,
        "chants": chants
    })

@app.get("/blogs")
def blog_list(request: Request):
    return templates.TemplateResponse(
        "blog_list.html",
        {
            "request": request,
            "blogs": load_all_blogs(),
        }
    )


@app.get("/categories")
def categories(request: Request):
    return templates.TemplateResponse(
        "categories.html",
        {
            "request": request,
            "categories": CATEGORY_DATA
        }
    )

@app.get("/contact")
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/blog/{slug}")
def blog_page(slug: str, request: Request):
    blog = load_blog_by_slug(slug)

    if not blog:
        return {"error": "Blog not found"}

    enroll = CATEGORY_FORMS.get(blog["category"])

    return templates.TemplateResponse(
        "blog.html",
        {
            "request": request,
            "blog": blog,
            "CATEGORY_DATA": CATEGORY_DATA,
            "enroll": enroll,
        }
    )
@app.get("/chant/{slug}")
def chant_page(slug: str, request: Request):

    chant = load_chant_by_slug(slug)

    if not chant:
        return {"error": "Chant not found"}

    return templates.TemplateResponse("chant_page.html", {
        "request": request,
        "chant": chant
    })


@app.get("/blogs")
def blog_list(request: Request):
    return templates.TemplateResponse(
        "blog_list.html",
        {
            "request": request,
            "blogs": load_all_blogs(),
        }
    )


@app.get("/categories")
def categories(request: Request):
    return templates.TemplateResponse(
        "categories.html",
        {
            "request": request,
            "categories": CATEGORY_DATA
        }
    )

@app.get("/workshops")
def workshops(request: Request):
    return templates.TemplateResponse("workshops.html",{"request":request})


@app.get("/payment")
def payment():
    return templates.TemplateResponse(form_url)


@app.get("/contact")
def contact():
    return templates.TemplateResponse("contact.html")