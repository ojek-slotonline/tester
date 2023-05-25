import requests
import json

url = "https://api-gw.iguverse.io/graphql"

headers = {
    "Content-Type": "application/json",
    "Origin": "https://mobile.iguverse.com",
    "Referer": "https://mobile.iguverse.com/",
    "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    "X-Api-Version": "27.0.0",
    "X-App-Version": "1.0.0",
    "X-Device-Id": "b63f1e39-6a12-46df-b039-923984ffab08",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzA4OTdhM2ItZTZhNS00YjlmLThhMTktZTQzYzM5ZWJlMTk2IiwiZW1haWwiOiJrYXlsYXphaHJhYWZpdmFAZ21haWwuY29tIn0sInNlc3Npb25JZCI6IjdhMTk0MDhmLTRiOWQtNDNmMi05NGE5LTkxMGMwODA4ZjViOCIsInN1YiI6IjcwODk3YTNiLWU2YTUtNGI5Zi04YTE5LWU0M2MzOWViZTE5NiIsImlhdCI6MTY4NTAwODQ5NCwiZXhwIjoxNjkyNzg0NDk0fQ.4WD98IWlzZJpkjreMAES0hgj23HKeT7CI5ba1KDgq78"
}

data = {
    "operationName": "Query",
    "variables": {},
    "query": """query Query {
    verificationTaskConfig {
        status
        canStart
        maxEnergyReward
        totalEnergyRewarded
        currentTask {
            id
            status
            failureReason
            maxEnergyReward
            energyRewarded
            isRated
            petExperienceRewards {
                id
                experienceIncrement
                pet {
                    id
                    name
                    image {
                        id
                        filename
                        url
                        thumbnailUrl
                        type
                        status
                        signedUploadUrl
                        metadata {
                            isFromCamera
                            isFromGallery
                            detectionResult {
                                label
                                confidence
                                __typename
                            }
                            backgroundId
                            text2ImageTaskId
                            __typename
                        }
                        updatedAt
                        createdAt
                        __typename
                    }
                    rank
                    tokenId
                    level
                    experience
                    health
                    likeCount
                                        dislikeCount
                    currentOwnerAddress
                    creatorAddress
                    lastTransferAt
                    updatedAt
                    createdAt
                    isMinted
                    cooldownExpiresAt
                    levelProgressPercentage
                    currentLevelMaxExperience
                    explorerUrl
                    levelUpAvailable
                    reviveAvailable
                    healthPercentage
                    dead
                    __typename
                }
                updatedAt
                createdAt
                __typename
            }
            socialTask {
                id
                platform
                platformUsername
                pet {
                    id
                    name
                    image {
                        id
                        filename
                        url
                        thumbnailUrl
                        type
                        status
                        signedUploadUrl
                        metadata {
                            isFromCamera
                            isFromGallery
                            detectionResult {
                                label
                                confidence
                                __typename
                            }
                            backgroundId
                            text2ImageTaskId
                            __typename
                        }
                        updatedAt
                        createdAt
                        __typename
                    }
                    rank
                    tokenId
                    level
                    experience
                    health
                    likeCount
                    dislikeCount
                    currentOwnerAddress
                    creatorAddress
                    lastTransferAt
                    updatedAt
                    createdAt
                    isMinted
                    cooldownExpiresAt
                    levelProgressPercentage
                    currentLevelMaxExperience
                    explorerUrl
                    __typename
                }
                __typename
            }
            updatedAt
            createdAt
            remainingVerificationAttempts
            __typename
        }
        tasks {
            id
            status
            failureReason
            maxEnergyReward
            energyRewarded
            isRated
            petExperienceRewards {
                id
                experienceIncrement
                pet {
                    id
                    name
                    image {
                        id
                        filename
                        url
                        thumbnailUrl
                        type
                        status
                        signedUploadUrl
                        metadata {
                            isFromCamera
                            isFromGallery
                            detectionResult {
                                label
                                confidence
                                __typename
                            }
                            backgroundId
                            text2ImageTaskId
                            __typename
                        }
                        updatedAt
                        createdAt
                        __typename
                    }
                    rank
                    tokenId
                    level
                    experience
                    health
                    likeCount
                    dislikeCount
                    currentOwnerAddress
                    creatorAddress
                    lastTransferAt
                    updatedAt
                    createdAt
                    isMinted
                    cooldownExpiresAt
                    levelProgressPercentage
                    currentLevelMaxExperience
                    explorerUrl
                    levelUpAvailable
                    reviveAvailable
                    healthPercentage
                    dead
                    __typename
                }
                updatedAt
                createdAt
                __typename
            }
            socialTask {
                id
                platform
                platformUsername
                pet {
                    id
                    name
                    image {
                        id
                        filename
                        url
                        thumbnailUrl
                        type
                        status
                        signedUploadUrl
                        metadata {
                            isFromCamera
                            isFromGallery
                            detectionResult {
                                label
                                confidence
                                __typename
                            }
                            backgroundId
                            text2ImageTaskId
                            __typename
                        }
                        updatedAt
                        createdAt
                        __typename
                    }
                    rank
                    tokenId
                    level
                    experience
                    health
                    likeCount
                    dislikeCount
                    currentOwnerAddress
                    creatorAddress
                    lastTransferAt
                    updatedAt
                    createdAt
                    isMinted
                    cooldownExpiresAt
                    levelProgressPercentage
                    currentLevelMaxExperience
                    explorerUrl
                    __typename
                }
                __typename
            }
            updatedAt
            createdAt
            remainingVerificationAttempts
            __typename
        }
        __typename
    }
}
"""
}

response = requests.post(url, headers=headers, data=json.dumps(data))


# To see the status code
print("Status Code: ", response.status_code)

# To see the response in json format
print("Response: ", response.json())

