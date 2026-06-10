def update_aircraft_status(aircraft):

    remaining = (
        aircraft.next_service_hours
        - aircraft.total_hours
    )

    if remaining <= 0:
        aircraft.status = "GROUNDED"

    elif remaining <= 10:
        aircraft.status = "MAINTENANCE_DUE"

    else:
        aircraft.status = "ACTIVE"

    aircraft.save()