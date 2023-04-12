# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from com.precisely.apis.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from com.precisely.apis.model.ahj import AHJ
from com.precisely.apis.model.ahj_list import AHJList
from com.precisely.apis.model.ahj_plus_psap_response import AHJPlusPSAPResponse
from com.precisely.apis.model.ah_jmailing_address import AHJmailingAddress
from com.precisely.apis.model.absentee_owner import AbsenteeOwner
from com.precisely.apis.model.accuracy import Accuracy
from com.precisely.apis.model.address import Address
from com.precisely.apis.model.address_time import AddressTime
from com.precisely.apis.model.address_type import AddressType
from com.precisely.apis.model.addresses_by_boundary_request import AddressesByBoundaryRequest
from com.precisely.apis.model.addresses_count import AddressesCount
from com.precisely.apis.model.addresses_dto import AddressesDTO
from com.precisely.apis.model.addresses_preferences import AddressesPreferences
from com.precisely.apis.model.addresses_response import AddressesResponse
from com.precisely.apis.model.amenities import Amenities
from com.precisely.apis.model.area import Area
from com.precisely.apis.model.area_code_info import AreaCodeInfo
from com.precisely.apis.model.assets_and_wealth_theme import AssetsAndWealthTheme
from com.precisely.apis.model.base_flood_elevation import BaseFloodElevation
from com.precisely.apis.model.basement_type import BasementType
from com.precisely.apis.model.basic_boundary import BasicBoundary
from com.precisely.apis.model.boundaries import Boundaries
from com.precisely.apis.model.boundary import Boundary
from com.precisely.apis.model.boundary_buffer import BoundaryBuffer
from com.precisely.apis.model.boundary_point import BoundaryPoint
from com.precisely.apis.model.buffer_relation import BufferRelation
from com.precisely.apis.model.buildg_class import BuildgClass
from com.precisely.apis.model.buildg_condition import BuildgCondition
from com.precisely.apis.model.buildg_features_sqft import BuildgFeaturesSqft
from com.precisely.apis.model.buildg_improve_area import BuildgImproveArea
from com.precisely.apis.model.buildg_improve_type import BuildgImproveType
from com.precisely.apis.model.buildg_quality import BuildgQuality
from com.precisely.apis.model.buildg_style import BuildgStyle
from com.precisely.apis.model.buildg_type import BuildgType
from com.precisely.apis.model.buildg_view import BuildgView
from com.precisely.apis.model.building_sqft_source import BuildingSqftSource
from com.precisely.apis.model.business_id import BusinessId
from com.precisely.apis.model.ca_exemptions import CaExemptions
from com.precisely.apis.model.candidate import Candidate
from com.precisely.apis.model.candidate_range import CandidateRange
from com.precisely.apis.model.candidate_range_unit import CandidateRangeUnit
from com.precisely.apis.model.carrier import Carrier
from com.precisely.apis.model.category import Category
from com.precisely.apis.model.category_metadata import CategoryMetadata
from com.precisely.apis.model.cbsa import Cbsa
from com.precisely.apis.model.census import Census
from com.precisely.apis.model.center import Center
from com.precisely.apis.model.city import City
from com.precisely.apis.model.common_geometry import CommonGeometry
from com.precisely.apis.model.community import Community
from com.precisely.apis.model.consistency_code import ConsistencyCode
from com.precisely.apis.model.construction import Construction
from com.precisely.apis.model.contact_details import ContactDetails
from com.precisely.apis.model.contact_person import ContactPerson
from com.precisely.apis.model.cooling_type import CoolingType
from com.precisely.apis.model.cost import Cost
from com.precisely.apis.model.county import County
from com.precisely.apis.model.coverage import Coverage
from com.precisely.apis.model.crime_boundary import CrimeBoundary
from com.precisely.apis.model.crime_index_theme import CrimeIndexTheme
from com.precisely.apis.model.crime_risk_by_address_batch_request import CrimeRiskByAddressBatchRequest
from com.precisely.apis.model.crime_risk_by_location_batch_request import CrimeRiskByLocationBatchRequest
from com.precisely.apis.model.crime_risk_preferences import CrimeRiskPreferences
from com.precisely.apis.model.crime_risk_response import CrimeRiskResponse
from com.precisely.apis.model.crime_risk_response_list import CrimeRiskResponseList
from com.precisely.apis.model.crs import Crs
from com.precisely.apis.model.demographics import Demographics
from com.precisely.apis.model.demographics_advanced_preferences import DemographicsAdvancedPreferences
from com.precisely.apis.model.demographics_advanced_request import DemographicsAdvancedRequest
from com.precisely.apis.model.demographics_geometry import DemographicsGeometry
from com.precisely.apis.model.demographics_geometry_crc import DemographicsGeometryCRC
from com.precisely.apis.model.demographics_themes_v2 import DemographicsThemesV2
from com.precisely.apis.model.depth import Depth
from com.precisely.apis.model.direction_geometry import DirectionGeometry
from com.precisely.apis.model.distance import Distance
from com.precisely.apis.model.distance_to_border import DistanceToBorder
from com.precisely.apis.model.distance_to_flood_hazard_address_request import DistanceToFloodHazardAddressRequest
from com.precisely.apis.model.distance_to_flood_hazard_location_request import DistanceToFloodHazardLocationRequest
from com.precisely.apis.model.distance_to_flood_hazard_response import DistanceToFloodHazardResponse
from com.precisely.apis.model.district_type import DistrictType
from com.precisely.apis.model.domestic_ultimate_business import DomesticUltimateBusiness
from com.precisely.apis.model.earthquake_date_time import EarthquakeDateTime
from com.precisely.apis.model.earthquake_event import EarthquakeEvent
from com.precisely.apis.model.earthquake_events_response import EarthquakeEventsResponse
from com.precisely.apis.model.earthquake_history import EarthquakeHistory
from com.precisely.apis.model.earthquake_location import EarthquakeLocation
from com.precisely.apis.model.earthquake_risk_by_address_request import EarthquakeRiskByAddressRequest
from com.precisely.apis.model.earthquake_risk_by_location_request import EarthquakeRiskByLocationRequest
from com.precisely.apis.model.earthquake_risk_response import EarthquakeRiskResponse
from com.precisely.apis.model.earthquake_risk_response_list import EarthquakeRiskResponseList
from com.precisely.apis.model.education_theme import EducationTheme
from com.precisely.apis.model.employee_count import EmployeeCount
from com.precisely.apis.model.employment_theme import EmploymentTheme
from com.precisely.apis.model.energy_type import EnergyType
from com.precisely.apis.model.error_code import ErrorCode
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.events_count import EventsCount
from com.precisely.apis.model.expenditure_theme import ExpenditureTheme
from com.precisely.apis.model.exterior_walls import ExteriorWalls
from com.precisely.apis.model.extra_feature_sqft import ExtraFeatureSqft
from com.precisely.apis.model.field import Field
from com.precisely.apis.model.fields_matching import FieldsMatching
from com.precisely.apis.model.fire_department import FireDepartment
from com.precisely.apis.model.fire_event import FireEvent
from com.precisely.apis.model.fire_events_response import FireEventsResponse
from com.precisely.apis.model.fire_history import FireHistory
from com.precisely.apis.model.fire_risk_by_address_request import FireRiskByAddressRequest
from com.precisely.apis.model.fire_risk_by_location_request import FireRiskByLocationRequest
from com.precisely.apis.model.fire_risk_response import FireRiskResponse
from com.precisely.apis.model.fire_risk_response_list import FireRiskResponseList
from com.precisely.apis.model.fire_shed import FireShed
from com.precisely.apis.model.fire_station import FireStation
from com.precisely.apis.model.fire_station_contact_details import FireStationContactDetails
from com.precisely.apis.model.fire_stations import FireStations
from com.precisely.apis.model.fireplace_type import FireplaceType
from com.precisely.apis.model.flood_hazard_preferences import FloodHazardPreferences
from com.precisely.apis.model.flood_risk_by_address_request import FloodRiskByAddressRequest
from com.precisely.apis.model.flood_risk_by_location_request import FloodRiskByLocationRequest
from com.precisely.apis.model.flood_risk_preferences import FloodRiskPreferences
from com.precisely.apis.model.flood_risk_response import FloodRiskResponse
from com.precisely.apis.model.flood_risk_response_list import FloodRiskResponseList
from com.precisely.apis.model.flood_zone import FloodZone
from com.precisely.apis.model.floor_type import FloorType
from com.precisely.apis.model.formatted_tax_address import FormattedTaxAddress
from com.precisely.apis.model.foundation import Foundation
from com.precisely.apis.model.free_or_reduced_price_lunches import FreeOrReducedPriceLunches
from com.precisely.apis.model.fuel_type import FuelType
from com.precisely.apis.model.garage_type import GarageType
from com.precisely.apis.model.geo_location_access_point import GeoLocationAccessPoint
from com.precisely.apis.model.geo_location_country import GeoLocationCountry
from com.precisely.apis.model.geo_location_ip_addr import GeoLocationIpAddr
from com.precisely.apis.model.geo_location_place import GeoLocationPlace
from com.precisely.apis.model.geo_location_state import GeoLocationState
from com.precisely.apis.model.geo_pos import GeoPos
from com.precisely.apis.model.geocode_address import GeocodeAddress
from com.precisely.apis.model.geocode_preferences import GeocodePreferences
from com.precisely.apis.model.geocode_request import GeocodeRequest
from com.precisely.apis.model.geocode_service_response import GeocodeServiceResponse
from com.precisely.apis.model.geocode_service_response_list import GeocodeServiceResponseList
from com.precisely.apis.model.geolocation_geometry import GeolocationGeometry
from com.precisely.apis.model.geometry import Geometry
from com.precisely.apis.model.geometry_crc import GeometryCRC
from com.precisely.apis.model.geometry_properties import GeometryProperties
from com.precisely.apis.model.get_city_state_province_api_input import GetCityStateProvinceAPIInput
from com.precisely.apis.model.get_city_state_province_api_input_row import GetCityStateProvinceAPIInputRow
from com.precisely.apis.model.get_city_state_province_api_options import GetCityStateProvinceAPIOptions
from com.precisely.apis.model.get_city_state_province_api_output import GetCityStateProvinceAPIOutput
from com.precisely.apis.model.get_city_state_province_api_request import GetCityStateProvinceAPIRequest
from com.precisely.apis.model.get_city_state_province_api_response import GetCityStateProvinceAPIResponse
from com.precisely.apis.model.get_postal_codes_api_input import GetPostalCodesAPIInput
from com.precisely.apis.model.get_postal_codes_api_input_row import GetPostalCodesAPIInputRow
from com.precisely.apis.model.get_postal_codes_api_options import GetPostalCodesAPIOptions
from com.precisely.apis.model.get_postal_codes_api_output import GetPostalCodesAPIOutput
from com.precisely.apis.model.get_postal_codes_api_output_user_fields import GetPostalCodesAPIOutputUserFields
from com.precisely.apis.model.get_postal_codes_api_request import GetPostalCodesAPIRequest
from com.precisely.apis.model.get_postal_codes_api_response import GetPostalCodesAPIResponse
from com.precisely.apis.model.global_ultimate_business import GlobalUltimateBusiness
from com.precisely.apis.model.grade_levels_taught import GradeLevelsTaught
from com.precisely.apis.model.greatschools import Greatschools
from com.precisely.apis.model.grid import Grid
from com.precisely.apis.model.health_theme import HealthTheme
from com.precisely.apis.model.heating_type import HeatingType
from com.precisely.apis.model.households_theme import HouseholdsTheme
from com.precisely.apis.model.housing_theme import HousingTheme
from com.precisely.apis.model.ipd_tax_by_address_batch_request import IPDTaxByAddressBatchRequest
from com.precisely.apis.model.ipd_tax_jurisdiction import IPDTaxJurisdiction
from com.precisely.apis.model.income_theme import IncomeTheme
from com.precisely.apis.model.index_variable import IndexVariable
from com.precisely.apis.model.individual_value_variable import IndividualValueVariable
from com.precisely.apis.model.interior_wall import InteriorWall
from com.precisely.apis.model.intermediate_points import IntermediatePoints
from com.precisely.apis.model.intersection import Intersection
from com.precisely.apis.model.intersection_response import IntersectionResponse
from com.precisely.apis.model.ip_info import IpInfo
from com.precisely.apis.model.ipd import Ipd
from com.precisely.apis.model.key_lookup_request import KeyLookupRequest
from com.precisely.apis.model.keys import Keys
from com.precisely.apis.model.land_use import LandUse
from com.precisely.apis.model.lat_long_fields import LatLongFields
from com.precisely.apis.model.life_style_theme import LifeStyleTheme
from com.precisely.apis.model.loc_code import LocCode
from com.precisely.apis.model.local_tax_geometry import LocalTaxGeometry
from com.precisely.apis.model.local_tax_preferences import LocalTaxPreferences
from com.precisely.apis.model.location import Location
from com.precisely.apis.model.location_time import LocationTime
from com.precisely.apis.model.magnitude import Magnitude
from com.precisely.apis.model.match import Match
from com.precisely.apis.model.matched_address import MatchedAddress
from com.precisely.apis.model.matrix import Matrix
from com.precisely.apis.model.mcd import Mcd
from com.precisely.apis.model.metadata_response import MetadataResponse
from com.precisely.apis.model.name import Name
from com.precisely.apis.model.neighborhoods_response import NeighborhoodsResponse
from com.precisely.apis.model.network import Network
from com.precisely.apis.model.organization_type import OrganizationType
from com.precisely.apis.model.other_rooms import OtherRooms
from com.precisely.apis.model.owner_vest_type import OwnerVestType
from com.precisely.apis.model.owners import Owners
from com.precisely.apis.model.pb_key_address_request import PBKeyAddressRequest
from com.precisely.apis.model.pb_key_response import PBKeyResponse
from com.precisely.apis.model.pb_key_response_list import PBKeyResponseList
from com.precisely.apis.model.poi_boundary_address_request import POIBoundaryAddressRequest
from com.precisely.apis.model.poi_boundary_location_request import POIBoundaryLocationRequest
from com.precisely.apis.model.poi_boundary_locations import POIBoundaryLocations
from com.precisely.apis.model.poi_boundary_preferences import POIBoundaryPreferences
from com.precisely.apis.model.poi_boundary_response import POIBoundaryResponse
from com.precisely.apis.model.poiby_geometry_request import POIByGeometryRequest
from com.precisely.apis.model.psap_response import PSAPResponse
from com.precisely.apis.model.parent_business import ParentBusiness
from com.precisely.apis.model.pbkey import Pbkey
from com.precisely.apis.model.phone_verification import PhoneVerification
from com.precisely.apis.model.phone_verification_output import PhoneVerificationOutput
from com.precisely.apis.model.place import Place
from com.precisely.apis.model.places_response import PlacesResponse
from com.precisely.apis.model.poi import Poi
from com.precisely.apis.model.poi_boundary import PoiBoundary
from com.precisely.apis.model.poi_classification import PoiClassification
from com.precisely.apis.model.poi_count import PoiCount
from com.precisely.apis.model.poi_count_request import PoiCountRequest
from com.precisely.apis.model.points import Points
from com.precisely.apis.model.pool_type import PoolType
from com.precisely.apis.model.population_theme import PopulationTheme
from com.precisely.apis.model.preferenc_time_zone import PreferencTimeZone
from com.precisely.apis.model.primary_zone import PrimaryZone
from com.precisely.apis.model.prior_sale_code import PriorSaleCode
from com.precisely.apis.model.prop_site_influene import PropSiteInfluene
from com.precisely.apis.model.properties import Properties
from com.precisely.apis.model.property_attributes import PropertyAttributes
from com.precisely.apis.model.property_geometry import PropertyGeometry
from com.precisely.apis.model.property_info_address_request import PropertyInfoAddressRequest
from com.precisely.apis.model.property_info_preferences import PropertyInfoPreferences
from com.precisely.apis.model.property_info_response import PropertyInfoResponse
from com.precisely.apis.model.property_info_responses import PropertyInfoResponses
from com.precisely.apis.model.proxy import Proxy
from com.precisely.apis.model.race_and_ethnicity_theme import RaceAndEthnicityTheme
from com.precisely.apis.model.range_variable import RangeVariable
from com.precisely.apis.model.rate import Rate
from com.precisely.apis.model.rate_center_response import RateCenterResponse
from com.precisely.apis.model.return_fields_descriptor import ReturnFieldsDescriptor
from com.precisely.apis.model.reverse_geocode_request import ReverseGeocodeRequest
from com.precisely.apis.model.risk import Risk
from com.precisely.apis.model.risk_address import RiskAddress
from com.precisely.apis.model.risk_geometry import RiskGeometry
from com.precisely.apis.model.risk_locations import RiskLocations
from com.precisely.apis.model.risk_preferences import RiskPreferences
from com.precisely.apis.model.risks_boundaries import RisksBoundaries
from com.precisely.apis.model.risks_crime_theme import RisksCrimeTheme
from com.precisely.apis.model.risks_geometry_crc import RisksGeometryCRC
from com.precisely.apis.model.road import Road
from com.precisely.apis.model.roof_cover_type import RoofCoverType
from com.precisely.apis.model.roof_frame_type import RoofFrameType
from com.precisely.apis.model.roof_shape_type import RoofShapeType
from com.precisely.apis.model.route_direction import RouteDirection
from com.precisely.apis.model.route_geometry import RouteGeometry
from com.precisely.apis.model.route_response import RouteResponse
from com.precisely.apis.model.sales_tax import SalesTax
from com.precisely.apis.model.sales_volume import SalesVolume
from com.precisely.apis.model.school import School
from com.precisely.apis.model.school_district import SchoolDistrict
from com.precisely.apis.model.school_profile import SchoolProfile
from com.precisely.apis.model.school_ranking import SchoolRanking
from com.precisely.apis.model.schools_near_by_response import SchoolsNearByResponse
from com.precisely.apis.model.segmentation import Segmentation
from com.precisely.apis.model.segmentation_themes import SegmentationThemes
from com.precisely.apis.model.shore_line_distance import ShoreLineDistance
from com.precisely.apis.model.sic import Sic
from com.precisely.apis.model.sic_metadata import SicMetadata
from com.precisely.apis.model.site_details import SiteDetails
from com.precisely.apis.model.situs_address import SitusAddress
from com.precisely.apis.model.special_purpose_district import SpecialPurposeDistrict
from com.precisely.apis.model.special_purpose_district_tax import SpecialPurposeDistrictTax
from com.precisely.apis.model.speed_limit import SpeedLimit
from com.precisely.apis.model.start_end_point import StartEndPoint
from com.precisely.apis.model.state import State
from com.precisely.apis.model.status import Status
from com.precisely.apis.model.stories import Stories
from com.precisely.apis.model.student_ethnicity import StudentEthnicity
from com.precisely.apis.model.supply_and_demand_theme import SupplyAndDemandTheme
from com.precisely.apis.model.tax_address import TaxAddress
from com.precisely.apis.model.tax_address_request import TaxAddressRequest
from com.precisely.apis.model.tax_county import TaxCounty
from com.precisely.apis.model.tax_district_response import TaxDistrictResponse
from com.precisely.apis.model.tax_district_response_list import TaxDistrictResponseList
from com.precisely.apis.model.tax_doc_type import TaxDocType
from com.precisely.apis.model.tax_exemption import TaxExemption
from com.precisely.apis.model.tax_geometry import TaxGeometry
from com.precisely.apis.model.tax_jurisdiction import TaxJurisdiction
from com.precisely.apis.model.tax_location_request import TaxLocationRequest
from com.precisely.apis.model.tax_locations import TaxLocations
from com.precisely.apis.model.tax_place import TaxPlace
from com.precisely.apis.model.tax_rate_address import TaxRateAddress
from com.precisely.apis.model.tax_rate_address_request import TaxRateAddressRequest
from com.precisely.apis.model.tax_rate_location_request import TaxRateLocationRequest
from com.precisely.apis.model.tax_rate_matched_address import TaxRateMatchedAddress
from com.precisely.apis.model.tax_rate_response import TaxRateResponse
from com.precisely.apis.model.tax_responses import TaxResponses
from com.precisely.apis.model.tax_sales_price_code import TaxSalesPriceCode
from com.precisely.apis.model.tax_state import TaxState
from com.precisely.apis.model.time import Time
from com.precisely.apis.model.timezone_address_request import TimezoneAddressRequest
from com.precisely.apis.model.timezone_geometry import TimezoneGeometry
from com.precisely.apis.model.timezone_location_request import TimezoneLocationRequest
from com.precisely.apis.model.timezone_response import TimezoneResponse
from com.precisely.apis.model.timezone_response_list import TimezoneResponseList
from com.precisely.apis.model.travel_boundaries import TravelBoundaries
from com.precisely.apis.model.travel_boundary import TravelBoundary
from com.precisely.apis.model.travel_cost_matrix_response import TravelCostMatrixResponse
from com.precisely.apis.model.type import Type
from com.precisely.apis.model.typeahead_location import TypeaheadLocation
from com.precisely.apis.model.typeahead_locations import TypeaheadLocations
from com.precisely.apis.model.typeahead_range import TypeaheadRange
from com.precisely.apis.model.typeahead_unit import TypeaheadUnit
from com.precisely.apis.model.unit import Unit
from com.precisely.apis.model.use_tax import UseTax
from com.precisely.apis.model.vacancy import Vacancy
from com.precisely.apis.model.validate_email_address_api_request import ValidateEmailAddressAPIRequest
from com.precisely.apis.model.validate_email_address_api_response import ValidateEmailAddressAPIResponse
from com.precisely.apis.model.validate_email_address_input import ValidateEmailAddressInput
from com.precisely.apis.model.validate_email_address_input_row import ValidateEmailAddressInputRow
from com.precisely.apis.model.validate_email_address_output import ValidateEmailAddressOutput
from com.precisely.apis.model.validate_mailing_address_input import ValidateMailingAddressInput
from com.precisely.apis.model.validate_mailing_address_input_row import ValidateMailingAddressInputRow
from com.precisely.apis.model.validate_mailing_address_options import ValidateMailingAddressOptions
from com.precisely.apis.model.validate_mailing_address_output import ValidateMailingAddressOutput
from com.precisely.apis.model.validate_mailing_address_premium_input import ValidateMailingAddressPremiumInput
from com.precisely.apis.model.validate_mailing_address_premium_input_row import ValidateMailingAddressPremiumInputRow
from com.precisely.apis.model.validate_mailing_address_premium_options import ValidateMailingAddressPremiumOptions
from com.precisely.apis.model.validate_mailing_address_premium_output import ValidateMailingAddressPremiumOutput
from com.precisely.apis.model.validate_mailing_address_premium_request import ValidateMailingAddressPremiumRequest
from com.precisely.apis.model.validate_mailing_address_premium_response import ValidateMailingAddressPremiumResponse
from com.precisely.apis.model.validate_mailing_address_pro_input import ValidateMailingAddressProInput
from com.precisely.apis.model.validate_mailing_address_pro_input_row import ValidateMailingAddressProInputRow
from com.precisely.apis.model.validate_mailing_address_pro_options import ValidateMailingAddressProOptions
from com.precisely.apis.model.validate_mailing_address_pro_output import ValidateMailingAddressProOutput
from com.precisely.apis.model.validate_mailing_address_pro_request import ValidateMailingAddressProRequest
from com.precisely.apis.model.validate_mailing_address_pro_response import ValidateMailingAddressProResponse
from com.precisely.apis.model.validate_mailing_address_request import ValidateMailingAddressRequest
from com.precisely.apis.model.validate_mailing_address_response import ValidateMailingAddressResponse
from com.precisely.apis.model.validate_mailing_address_uscanapi_input import ValidateMailingAddressUSCANAPIInput
from com.precisely.apis.model.validate_mailing_address_uscanapi_input_row import ValidateMailingAddressUSCANAPIInputRow
from com.precisely.apis.model.validate_mailing_address_uscanapi_options import ValidateMailingAddressUSCANAPIOptions
from com.precisely.apis.model.validate_mailing_address_uscanapi_output import ValidateMailingAddressUSCANAPIOutput
from com.precisely.apis.model.validate_mailing_address_uscanapi_request import ValidateMailingAddressUSCANAPIRequest
from com.precisely.apis.model.validate_mailing_address_uscanapi_response import ValidateMailingAddressUSCANAPIResponse
from com.precisely.apis.model.validate_phone_number_api_request import ValidatePhoneNumberAPIRequest
from com.precisely.apis.model.validate_phone_number_api_request_input import ValidatePhoneNumberAPIRequestInput
from com.precisely.apis.model.validate_phone_number_api_request_input_row import ValidatePhoneNumberAPIRequestInputRow
from com.precisely.apis.model.water_body import WaterBody
from com.precisely.apis.model.water_body_response import WaterBodyResponse
from com.precisely.apis.model.zones_address import ZonesAddress
from com.precisely.apis.model.zones_boundary_geometry import ZonesBoundaryGeometry
from com.precisely.apis.model.zones_contact_details import ZonesContactDetails
from com.precisely.apis.model.zones_geometry import ZonesGeometry
from com.precisely.apis.model.zones_parent_business import ZonesParentBusiness
from com.precisely.apis.model.zones_poi import ZonesPoi
from com.precisely.apis.model.zones_poi_classification import ZonesPoiClassification
from com.precisely.apis.model.zones_poi_geometry import ZonesPoiGeometry
from com.precisely.apis.model.zones_sic import ZonesSic
