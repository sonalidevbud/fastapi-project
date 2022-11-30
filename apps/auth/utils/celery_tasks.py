from apps.sast.crud.shared_connected_providers import update_connection_tokens


@celery_app.task()
def update_connection_tokens():
    update_connection_tokens()