import requests

GET_ROOM_TYPES = """
        query publicAPIGetPropertyRoomType(
            $propertyId: ID!
            $tenancyOptionId: ID
            $availableForBook: Boolean = true
        ) {
            node(id: $propertyId) {
            ... on Property {
                roomTypes(availableForBook: $availableForBook) {
                id
                name
                category
                bathroomType
                bathroomArrangement
                kitchenType
                kitchenArrangement
                count
                hasPrice
                minPricePerNight
                minPriceForBillingCycle
                maxNumOfBedsInFlat
                marketingPrice(tenancyOptionId: $tenancyOptionId) {
                    marketingPrice
                    marketingInstallmentNumber
                }
                availabilityInfos {
                    academicYear {
                    id
                    name
                    fromYear
                    toYear
                    isEnabled
                    isCurrent
                    }
                    tenancyOptionInfos {
                    tenancyOption {
                        id
                        academicYearId
                        name
                        tenancyType
                        startDateType
                        startDate
                        endDateType
                        endDate
                        status
                        tenancyLengthType
                        tenancyLength
                    }
                    numberOfAvailableBeds
                    minPricePerNight
                    minPriceForBillingCycle
                    }
                }
                }
            }
            }
        }
        """
data = {
    "query": GET_ROOM_TYPES,
    "variables": {"propertyId": "eyJ0eXBlIjoiUHJvcGVydHkiLCJpZCI6OX0="},
}

response = requests.post(url="https://gateway.project-g66.com/graphql", json=data)

print(response.json())
