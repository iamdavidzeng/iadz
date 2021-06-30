# -*- coding: utf-8 -*-


import re

stream = """
type MsgCenterLandlordContact implements Node {
    id: ID!
    firstName: String!
    lastName: String!
    userUuid: NonEmptyString!
    liveChatEnabled: Boolean!
    online: Boolean
}

input MsgCenterLandlordContact implements 123 {
    id: ID! @decodeID(type: "Landlord", required: true)
    firstName: String!
    lastName: String!
    userUuid: NonEmptyString!
    liveChatEnabled: Boolean!
    online: Boolean
    pageNumber: Int = 1
    pageSize: Int = 10
    edges: [Foo]
}
"""

enums = """
// Enums Resovlers for downcase
export const enumsResovlers = {
  ReconciliationBulkUpdateRecordStatusEnum: {
    NEW: 'new',
    IN_PROCESS: 'in_process',
    DONE: 'done',
  },
  TenancyAgreementTimeTypeEnum: {
    ANYTIME: 'anytime',
    FIXED: 'fixed',
  },
  TenancyAgreementUnitEnum: {
    DAY: 'day',
  },
  TenancyAgreementFieldEnum: {
    MOVE_IN_DATE: 'move_in_date',
  },
  TenancyAgreementCalculateTypeEnum: {
    BEFORE: 'before',
    BEFORE_OR_ON: 'before_or_on',
    ON: 'on',
    AFTER: 'after',
    AFTER_OR_ON: 'after_or_on',
  },
  ApCategory: {
    STANDARD: 'standard',
    KEY: 'key',
  },
  ScopeOperate: {
    CREATE: 'c',
    READ: 'r',
    UPDATE: 'u',
    DELETE: 'd',
  },
  InvoicingFrequency: {
    MONTHLY: 'monthly',
    QUARTERLY: 'quarterly',
    YEARLY: 'yearly',
  },
  ReconciliationPreference: {
    LANDLORD_PORTAL: 'll_portal',
    EMAIL_CSV: 'email_csv',
    NOT_SPECIFIC: 'not_specific',
  },
  // sturents, appfolio, realpage, salesforce, rentcafe, tenantcloud
  // These were added before, so they don't correspond to the key
  SystemProvider: {
    ENTRATA: 'entrata',
    KINETIC: 'kinetic',
    ON_SITE: 'on_site',
    ONESITE: 'one_site',
    PEX: 'pex',
    STAR_REZ: 'star_rez',
    TCAS: 'tcas',
    OWN_SYSTEM: 'own_system',
    BUILD_IN_HOUSE_LAMS: 'build_in_house_lams',
    BUILT_IN_HOUSE: 'build_in_house',
    GRADPAD: 'gradpad',
    LEASE_HAWK: 'lease_hawk',
    ONESITE_YARDI: 'onesite_yardi',
    ROOM_SERVICE_OCCAM: 'room_service_occam',
    SEARCH_QUEST: 'search_quest',
    SIRVOY: 'sirvoy',
    STU_RENTS: 'sturents',
    OCCAM: 'occam',
    APP_FOLIO: 'appfolio',
    REAL_PAGE: 'realpage',
    NO_SYSTEM: 'no_system',
    SALES_FORCE: 'salesforce',
    RENT_CAFE: 'rentcafe',
    YARDI: 'yardi',
    TENANT_CLOUD: 'tenantcloud',
    OTHER: 'other',
    RENTMANAGER: 'rentmanager',
    RES_MAN: 'res_man',
    INNSOFT: 'innsoft',
    SYNXIS: 'synxis',
    SITEMINDER: 'siteminder',
    MRI_SOFTWARE: 'mri_software',
    LEASE_LABS: 'lease_labs',
    CLOUDBEDS: 'cloudbeds',
  },
  LandlordContactSearchField: {
    EMAIL: 'email',
  },
  PropertyDraftStatus: {
    PENDING: 'pending',
    APPROVED: 'approved',
    REJECTED: 'rejected',
    EXPIRED: 'expired',
  },
  ContractStatus: {
    ACTIVE: 'active',
    INACTIVE: 'inactive',
    EXPIRE: 'expire',
  },
  ContractStage: {
    PROSPECT: 'prospect',
    CONTACTED: 'contacted',
    DUALLY_SIGNED: 'dually_signed',
    LOST: 'lost',
    CHANGE_OWNERSHIP: 'change_ownership',
    VERBAL: 'verbal',
    LEGAL: 'legal',
    SENT_CONTRACTS: 'sent_contracts',
    SIGNED: 'signed',
    NOT_LISTING: 'not_listing',
  },
  UpdateContractStage: {
    PROSPECT: 'prospect',
    CONTACTED: 'contacted',
    DUALLY_SIGNED: 'dually_signed',
    LOST: 'lost',
    CHANGE_OWNERSHIP: 'change_ownership',
  },
  CapType: {
    LENGTH: 'length',
    VALUE: 'value',
  },
  TenancyUnit: {
    DAYS: 'days',
    WEEKS: 'weeks',
    MONTHS: 'months',
  },
  CommissionType: {
    PERCENTAGE: 'percentage',
    VALUE: 'value',
  },
  CategoryType: {
    FLAT_FEE: 'flat_fee',
    NUM_BOOKINGS: 'num_bookings',
    TENANCY_LENGTH: 'tenancy_length',
    REBOOKERS_COMMISSION: 'rebookers_commission',
  },
  DisplayRegion: {
    ALL: 'all',
    CN: 'cn',
    ROW: 'row',
  },
  PropertyLinkLabel: {
    OVERALL: 'overall',
    PROPERTY: 'property',
  },
  PropertyLinkArea: {
    GENERAL: 'general',
    BUILDING_EXTERIOR: 'building_exterior',
    COMMON_INDOOR_SPACES: 'common_indoor_spaces',
    COMMON_OUTDOOR_SPACES: 'common_outdoor_spaces',
  },
  CancellationPeriod: {
    NON_REFUNDABLE: 'non_refundable',
    BEFORE_MOVE_IN_CALENDAR_DAYS_0: '0_calendar_days_before_move_in',
    BEFORE_MOVE_IN_CALENDAR_DAYS_7: '7_calendar_days_before_move_in',
    BEFORE_MOVE_IN_CALENDAR_DAYS_14: '14_calendar_days_before_move_in',
    BEFORE_MOVE_IN_CALENDAR_DAYS_30: '30_calendar_days_before_move_in',
    BEFORE_MOVE_IN_CALENDAR_DAYS_60: '60_calendar_days_before_move_in',
    BEFORE_MOVE_IN_CALENDAR_DAYS_90: '90_calendar_days_before_move_in',
  },
  FreeCancellationPeriod: {
    HOURS_24: '24_hours',
    HOURS_48: '48_hours',
    HOURS_72: '72_hours',
    BUSINESS_DAYS_5: '5_business_days',
    CALENDAR_DAYS_0: '0_calendar_days',
    CALENDAR_DAYS_3: '3_calendar_days',
    CALENDAR_DAYS_5: '5_calendar_days',
    CALENDAR_DAYS_7: '7_calendar_days',
    CALENDAR_DAYS_14: '14_calendar_days',
    CALENDAR_DAYS_28: '28_calendar_days',
    CALENDAR_DAYS_30: '30_calendar_days',
    CALENDAR_DAYS_60: '60_calendar_days',
    CALENDAR_DAYS_90: '90_calendar_days',
    UNTIL_CHECK_IN_DAY: 'until_check_in_day',
    UNTIL_THE_STUDENT_PAYS_FOR_THE_RENT: 'until_the_student_pays_for_the_rent',
    NO_COOLING_OFF_PERIOD: 'no_cooling_off_period',
    OTHER: 'other',
  },
  MutationAction: {
    DELETE: 'delete',
    UPDATE: 'update',
    INSERT: 'insert',
  },
  FacilityMutationAction: {
    DELETE: 'delete',
    INSERT: 'insert',
  },
  UniversityMutationAction: {
    DELETE: 'delete',
    INSERT: 'insert',
  },
  RoomType: {
    SQM: 'sqm',
    SQFT: 'sqft',
  },
  BedSizeType: {
    UNIFIED: 'unified',
    DIFFERENT: 'different',
  },
  DualOccupancy: {
    DUAL_OCCUPANCY_ALLOWED: 'dual_occupancy_allowed',
    FREE_DUAL_OCCUPANCY: 'free_dual_occupancy',
    CHARGED_DUAL_OCCUPANCY: 'charged_dual_occupancy',
    DUAL_OCCUPANCY_NOT_ALLOWED: 'dual_occupancy_not_allowed',
  },
  KitchenArrangement: {
    PRIVATE: 'private',
    SHARED: 'shared',
  },
  BedType: {
    SINGLE_BED: 'single_bed',
    DOUBLE_BED: 'double_bed',
    SMALL_DOUBLE_BED: 'small_double_bed',
    KING_BED: 'king_bed',
    KING_SINGLE_BED: 'king_single_bed',
    CALIFORNIA_KING_BED: 'california_king_bed',
    GRAND_KING_BED: 'grand_king_bed',
    QUEEN_BED: 'queen_bed',
    KING_SIZE_BED: 'king_size_bed',
    TWIN_BED: 'twin_bed',
    BUNK_BED: 'bunk_bed',
  },
  UnitTypeCategory: {
    ENSUITE_ROOM: 'ensuite-room',
    ENTIRE_PLACE: 'entire-place',
    PRIVATE_ROOM: 'private-room',
    SHARED_ROOM: 'shared-room',
    STUDIO: 'studio',
  },
  BathroomTypeCategory: {
    PRIVATE_ENSUITE: 'private-ensuite',
    PRIVATE_NON_ENSUITE: 'private-non-ensuite',
    SHARED_ENSUITE: 'shared-ensuite',
    SHARED_NON_ENSUITE: 'shared-non-ensuite',
    MIXED: 'mixed',
  },
  RoomArrangement: {
    CLUSTER: 'cluster',
    APARTMENT: 'apartment',
    HOTEL_STYLE: 'hotel-style',
  },
  GenderMix: {
    MALE_ONLY: 'male-only',
    FEMALE_ONLY: 'female-only',
    MIXED: 'mixed',
  },
  DietaryPreference: {
    VEGETARIAN: 'vegetarian',
  },
  SmokingPreference: {
    NON_SMOKING: 'non-smoking',
    SMOKING: 'smoking',
  },
  AreaUnit: {
    SQFT: 'sqft',
    M2: 'm2',
  },
  PropertyState: {
    AVAILABLE_WITH_PRICE: 'available_with_price',
    AVAILABLE: 'available',
    COMING_SOON: 'coming_soon',
    SOLD_OUT: 'sold_out',
    INACTIVE: 'inactive',
  },
  FacilityType: {
    PROPERTY: 'property',
    UNIT_TYPE: 'unit_type',
  },
  AuditPropertyModel: {
    PROPERTY: 'Property',
    ADDRESS: 'Address',
    PROPERTY_ADDRESS: 'PropertyAddress',
    PROPERTY_FACILITY: 'PropertyFacility',
    UNIT_TYPE: 'UnitType',
    LISTING: 'Listing',
  },

  // listing
  ListingState: {
    AVAILABLE_WITH_PRICE: 'available_with_price',
    AVAILABLE: 'available',
    COMING_SOON: 'coming_soon',
    SOLD_OUT: 'sold_out',
    INACTIVE: 'inactive',
  },

  // gallery
  VideoLocalsInput: {
    ALL:
      'en-us,en-gb,vi-vn,ja-jp,ko-kr,zh-hk,zh-tw,zh-cn,th-th,fr-fr,it-it,de-de,es-es,es-la,pt-br,el-gr,el-cy,tr-tr,ru-ru',
    ROW:
      'en-us,en-gb,zh-tw,zh-hk,ko-kr,ja-jp,th-th,vi-vn,de-de,el-gr,el-cy,es-es,es-la,fr-fr,it-it,pt-br,ru-ru,tr-tr',
    CN: 'zh-cn',
  },
  // propertyDraft
  PropertyDraftCategory: {
    DETAIL: 'detail',
    GALLERY: 'gallery',
  },

  // landlord
  LandlordAccountLevel: {
    PROPERTY: 'property',
    LANDLORD: 'landlord',
  },

  ReconciliationFrequency: {
    MONTHLY: 'monthly',
    QUARTERLY: 'quarterly',
  },
  OpportunityCaseTopic: {
    STUDENT_CANCELLATION: 'student_cancellation',
    STUDENT_NO_SHOW: 'student_no_show',
    INCOMPLETE: 'incomplete',
    NO_BOOKING_PROOF: 'no_booking_proof',
    SHORT_STAY: 'short_stay',
    MISCELLANEOUS: 'miscellaneous',
  },
  BookingPendingNote: {
    STUDENT_CANCELLATION: 'student_cancellation',
    STUDENT_NO_SHOW: 'student_no_show',
    INCOMPLETE: 'incomplete',
    NO_BOOKING_PROOF: 'no_booking_proof',
    AGENT_CLASH: 'agent_clash',
    CAP_REACHED: 'cap_reached',
    ZERO_COMMISSION: 'zero_commission',
    REBOOKER: 'rebooker',
    SHORT_STAY: 'short_stay',
    BREAK_LEASE: 'break_lease',
    BOOKING_PROCESS: 'booking_process',
    MISCELLANEOUS: 'miscellaneous',
    TENANCY_TAKEOVER: 'tenancy_takeover',
  },

  // payments
  PaymentsTermsAndConditionsStatus: {
    ACTIVE: 'active',
    INACTIVE: 'inactive',
    EXPIRED: 'expired',
  },
};
"""


def gen_enum(source_str: str):
    enum_name = ""
    result = ""
    lines = [line.strip() for line in source_str.split("\n") if line.strip()]
    for line in lines:
        line = line.strip()
        if re.match(r"\w+: {", line):
            enum_name = re.match(r"(?P<name>\w+): {", line).group("name")
            line = f"export enum {line.replace(':', '')}"
        elif re.match(r".+: .+,", line):
            line = line.replace(":", " =")
        elif re.match(r"},", line):
            line = """}
registerEnumType(%s, {
    name: '%s',
});""" % (
                enum_name,
                enum_name,
            )
        result += f"{line} \n"
    print(result)


def convert(match):
    for group in match.groups():
        lines = group.split("\n")
        for index, line in enumerate(lines):
            prefix = ""
            if "type " in line:
                prefix = "@ObjectType()\n"
                line_list = line.split(" ")
                line = " ".join(["  export class", line_list[1], line_list[-1], "\n"])

            if "input" in line:
                prefix = "@ArgsType()\n"
                line_list = line.split(" ")
                line = " ".join(["  export class", line_list[1], line_list[-1], "\n"])

            if ":" in line:
                try:
                    type_ = line.strip().split(" ")[1]
                except Exception as e:
                    print(e)
                    print(f"line: {line}")
                prefix = f"  @Field(() => {type_})\n  "

                if "!" in line:
                    type_ = type_.replace("!", "")
                    nullable = "{ nullable: false }"
                    prefix = f"  @Field(() => {type_}, {nullable})\n  "

            new_line = (
                prefix
                + line.strip()
                .replace("!", "")
                .replace("ID", "string")
                .replace("Int", "number")
                .replace("NonEmptyString", "string")
                .replace("[", "")
                .replace("]", "[]")
                .replace("Datetime", "Date")
                .replace("Boolean", "boolean")
                .replace("Json", "GraphQLJSON")
                + "\n"
            )
            lines[index] = new_line
    return "\n".join(lines)


parser = re.compile(r"(\w+[\w\s]+\{[\w\s\:\!\@\(\)\"\,\=\[\]]+\})")
result = parser.sub(convert, stream)
print(f"result: {result}")

# gen_enum(enums)


# with open("foo.gql") as f, open("bar.ts", "w") as w:

#     stream = f.read()

#     parser = re.compile(r"(\w+[\w\s]+\{[\w\s\:\!\@\(\)\"\,\=\[\]]+\})")
#     new_stream = parser.sub(convert, stream)

#     w.write(new_stream)
