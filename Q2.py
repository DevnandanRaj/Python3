members=[
    {"name": "Alice", "preferred_genre": "Romance"},
    {"name": "Bob", "preferred_genre": "Sci-Fi"}
]

books=[
    {"title": "Love in the Rain", "genre": "Romance"},
    {"title": "historical times", "genre": "History"}
]


def rec_books(members, books):
    rec = []
    for member in members:
        member_name=member["name"]
        preferred_genre=member["preferred_genre"]
        
        rec_book= next((book["title"] for book in books if book["genre"] == preferred_genre), None)
        if rec_book:
            rec.append({"member": member_name, "book": rec_book })
        else:
            rec.append({"member": member_name, "book": None})
    return rec


ans= rec_books(members,books)
print(ans)