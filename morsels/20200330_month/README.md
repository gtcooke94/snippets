By the time I reached the last bonus for `__slots__`, immutability, and hashability, I realized that `dataclass` would be a perfect thing to use here. With `frozen=True`, I get immutability and hashability for free! The only difficult thing I had to deal with was setting the  `first_day` and `last_day` inside the realm of what is allowed by `dataclasses`. This is when I found `__post_init__`, which completely solved my problem.

We could actually use `ordering=True` on the dataclass and not have to worry about comparison operators either!
