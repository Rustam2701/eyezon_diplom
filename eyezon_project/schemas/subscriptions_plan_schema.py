subscription_plans = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {
                "type": "integer"
            },
            "type": {
                "type": "string"
            },
            "name": {
                "type": "string"
            },
            "icon": {
                "type": "string",
                "enum": [
                    "InfoOutlined"
                ]
            },
            "description": {
                "type": "string"
            },
            "contractPrice": {
                "type": "boolean"
            },
            "benefits": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "enum": [
                                "SUBSCRIPTION_PLAN.BENEFIT.EXTENDED_STATISTICS",
                                "SUBSCRIPTION_PLAN.BENEFIT.WIDGET_PERSONALIZATION",
                                "SUBSCRIPTION_PLAN.BENEFIT.REQUEST_ROUTING",
                                "SUBSCRIPTION_PLAN.BENEFIT.RECORDING_SESSIONS",
                                "SUBSCRIPTION_PLAN.BENEFIT.PERSONAL_MANAGER",
                                "SUBSCRIPTION_PLAN.BENEFIT.PRIORITY_TECHNICAL_SUPPORT",
                                "SUBSCRIPTION_PLAN.BENEFIT.UNLIMITED_LOGIN_POINTS",
                                "SUBSCRIPTION_PLAN.BENEFIT.ACCESS_TO_EYEZON_360",
                                "SUBSCRIPTION_PLAN.BENEFIT.API_ACCESS",
                                "SUBSCRIPTION_PLAN.BENEFIT.SDK_ACCESS"
                            ]
                        },
                        "tooltip": {
                            "type": "string",
                            "enum": [
                                "SUBSCRIPTION_PLAN.BENEFIT.EXTENDED_STATISTICS.TOOLTIP",
                                "SUBSCRIPTION_PLAN.BENEFIT.WIDGET_PERSONALIZATION.TOOLTIP",
                                "SUBSCRIPTION_PLAN.BENEFIT.REQUEST_ROUTING.TOOLTIP",
                                "SUBSCRIPTION_PLAN.BENEFIT.RECORDING_SESSIONS.TOOLTIP",
                                "SUBSCRIPTION_PLAN.BENEFIT.PERSONAL_MANAGER.TOOLTIP",
                                "SUBSCRIPTION_PLAN.BENEFIT.PRIORITY_TECHNICAL_SUPPORT.TOOLTIP",
                                "SUBSCRIPTION_PLAN.BENEFIT.UNLIMITED_LOGIN_POINTS.TOOLTIP",
                                "SUBSCRIPTION_PLAN.BENEFIT.ACCESS_TO_EYEZON_360.TOOLTIP",
                                "SUBSCRIPTION_PLAN.BENEFIT.API_ACCESS.TOOLTIP",
                                "SUBSCRIPTION_PLAN.BENEFIT.SDK_ACCESS.TOOLTIP"
                            ]
                        },
                        "available": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "name",
                        "tooltip",
                        "available"
                    ]
                }
            },
            "trialStreams": {
                "type": "integer"
            },
            "trialDays": {
                "type": "integer"
            },
            "price": {
                "type": "string"
            },
            "createdAt": {
                "type": "string"
            },
            "updatedAt": {
                "type": "string"
            }
        },
        "required": [
            "id",
            "type",
            "name",
            "icon",
            "description",
            "contractPrice",
            "benefits",
            "trialStreams",
            "trialDays",
            "price",
            "createdAt",
            "updatedAt"
        ]
    }
}
