def find_meeting_point(distance, speed1, speed2) -> float:
    """Return the distance for moving object at `speed1` initially at
    point 0 at which it meets moving object at `speed2` going towards moving
    object of `speed1` from an initial distance `distance`."""
    time_taken = distance / (speed1 + speed2)
    return speed1 * time_taken  # distance for speed 1
