def validate_isci(ad, maas):

    if ad is None or ad.strip() == "":
        raise ValueError("Ad hissesi boş  ola bilməz")

    if maas <= 0:
        raise ValueError("Maaş 0-dan böyük olmalıdır")

    return True