def generate_metadata(filename):
    base = filename.replace(".mp4", "")
    base = base.replace("_", " ").replace("720P HD", "").strip()

    title = f"😱 {base[:60]}... Must Watch!"

    return {
        "title": title,
        "description": f"Watch till end 🔥\n\n#shorts #viral",
        "tags": ["shorts", "viral", "trending"]
    }