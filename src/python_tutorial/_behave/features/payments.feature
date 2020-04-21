Feature: Stirpe Payment

    As a student
    I want to secure a bed by reserving and paying in GIBBS

    Background: Services are up and running
        Given Payments service is running

    Scenario: Successful healthcheck
        When I send a healthcheck request to payments-service
        Then I should get successful response


    Scenario: Get transaction successfully
        Given There is one transaction
            | transaction_record_id | amount | currency |
            | 2                     | 100    | GBP      |
        When I get the transaction by transaction_record_id 2
        Then I should the right transaction
            """
            {
                "transaction_record_id": 2,
                "charge_id": null,
                "amount": 100,
                "currency": "GBP"
            }
            """