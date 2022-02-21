#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2022 https://github.com/Oops19
#

from inappropriate_drone_recordings.modinfo import ModInfo
from interactions.privacy import PrivacyService
from sims4communitylib.utils.common_injection_utils import CommonInjectionUtils
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog

log: CommonLog = CommonLogRegistry.get().register_log(f"{ModInfo.get_identity().author}_{ModInfo.get_identity().name}", ModInfo.get_identity().name)
log.enable()
log.info("Inappropriate Drone Recordings starting ...")

'''
This mod override two functions. 'Drone' will no longer be monitored and stop if sims do inappropriate things.
class PrivacyService(Service):
    def add_vehicle_to_monitor(self, vehicle):
        self._potential_vehicles_to_check.add(vehicle)

    def remove_vehicle_to_monitor(self, vehicle):
        self._potential_vehicles_to_check.discard(vehicle)
'''


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), PrivacyService, PrivacyService.add_vehicle_to_monitor.__name__)
def o19_add_vehicle_to_monitor(original, self, vehicle, *args, **kwargs):
    if 'Drone' in f'{vehicle}':
        log.debug(f'o19_add_vehicle_to_monitor({vehicle}) ... skipping')
    else:
        log.debug(f'o19_add_vehicle_to_monitor({vehicle})')
        original(self, vehicle, *args, **kwargs)


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), PrivacyService, PrivacyService.remove_vehicle_to_monitor.__name__)
def o19_remove_vehicle_to_monitor(original, self, vehicle, *args, **kwargs):
    if 'Drone' in f'{vehicle}':
        log.debug(f'o19_remove_vehicle_to_monitor({vehicle}) ... skipping')
    else:
        log.debug(f'o19_remove_vehicle_to_monitor({vehicle})')
        original(self, vehicle, *args, **kwargs)


log.info("Inappropriate Drone Recordings started.")
log.disable()

