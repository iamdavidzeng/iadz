# -*- coding: utf-8 -*-


def is_commute_times_update_required(status, changed):
    if (
        status == "published"
        and (
            not changed
            or "status" in changed
            or "latitude" in changed
            or "longitude" in changed
        )
    ) or (status == "unpublished" and "status" in changed):
        return True
    return False


if __name__ == "__main__":

    paylod = {"status": "unpublished", "changed": ["status", "updated_by"]}

    update_or_not = is_commute_times_update_required(
        paylod["status"], paylod["changed"]
    )

    print(f"Updated: {update_or_not}")
