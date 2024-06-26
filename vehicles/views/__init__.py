from .frontend import vehicle_list,fuel_disbursed,fuel_received,maintenance_list,mileage_list,index
from .users import user_logout_view,UserLoginView
from .fuel import FuelDisbursementCreate, FuelDisbursementDetail, FuelDisbursementList,SubProgrammeAPIView,ProgrammeAPIView,UpdateFuelDisbursement
from .maintenance import MaintenanceCreate,MaintenanceClose,UpdateMaintenance,MaintenanceDetail,MaintenanceList,MaintenanceApiList
from .vehicles import VehicleCreate,VehicleDetail,vehicles_list,ProvinceAPIView,LocationAPIView,UpdateVehicle,UserProfileList,StatusAPIView,VehicleDetailsAPIView,\
    check_vehicle_exists,vehicles_in_user_province,FuelTypeAPIView
from .mileage import MileageRecordCreate,MileageRecordDetail,MileageRecordList,UpdateMileageRecord,MileageRecordApiList