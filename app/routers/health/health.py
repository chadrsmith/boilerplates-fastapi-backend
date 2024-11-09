### HEALTH CHECK ROUTE ###
async def get_sys_health():
    return { "status": "healthy" }