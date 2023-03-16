from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore

from managers.scheduler_manger import manager_update


def start():
    scheduler=BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    register_events(scheduler)

    @scheduler.scheduled_job('cron',day="*/7", name='manager_update', max_instances=1)
    def auto_check():
        manager_update()

    scheduler.start()