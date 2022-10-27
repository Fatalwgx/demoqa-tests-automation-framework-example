import selene


def add(element: selene.Element, *tags: str):
    for tag in tags:
        element.type(tag).press_enter()
