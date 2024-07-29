"""All requests, responses and API models defined for the AI Horde API."""

from horde_sdk.ai_horde_api.apimodels._documents import (
    AIHordeDocumentRequestMixin,
    AIHordeGetPrivacyPolicyRequest,
    AIHordeGetSponsorsRequest,
    AIHordeGetTermsRequest,
    DocumentFormat,
    HordeDocument,
)
from horde_sdk.ai_horde_api.apimodels._find_user import (
    FindUserRequest,
)
from horde_sdk.ai_horde_api.apimodels._kudos import (
    KudosTransferRequest,
    KudosTransferResponse,
)
from horde_sdk.ai_horde_api.apimodels._stats import (
    ImageStatsModelsRequest,
    ImageStatsModelsResponse,
    ImageStatsModelsTotalRequest,
    ImageStatsModelsTotalResponse,
    SinglePeriodImgStat,
    SinglePeriodTxtStat,
    StatsModelsTimeframe,
    TextStatsModelResponse,
    TextStatsModelsRequest,
    TextStatsModelsTotalRequest,
    TextStatsModelsTotalResponse,
)
from horde_sdk.ai_horde_api.apimodels._status import (
    ActiveModel,
    ActiveModelLite,
    AIHordeHeartbeatRequest,
    AIHordeHeartbeatResponse,
    HordeModes,
    HordePerformanceRequest,
    HordePerformanceResponse,
    HordeStatusModelsAllRequest,
    HordeStatusModelsAllResponse,
    HordeStatusModelsSingleRequest,
    HordeStatusModelsSingleResponse,
    Newspiece,
    NewsRequest,
    NewsResponse,
)
from horde_sdk.ai_horde_api.apimodels._styles import ResponseModelStylesUser
from horde_sdk.ai_horde_api.apimodels._users import (
    ActiveGenerations,
    ContributionsDetails,
    ListUsersDetailsRequest,
    ListUsersDetailsResponse,
    ModifyUser,
    ModifyUserReply,
    ModifyUserRequest,
    ModifyUserResponse,
    MonthlyKudos,
    SingleUserDetailsRequest,
    UsageDetails,
    UserAmountRecords,
    UserDetailsResponse,
    UserKudosDetails,
    UserRecords,
    UserThingRecords,
    _ModifyUserBase,
)
from horde_sdk.ai_horde_api.apimodels.alchemy._async import (
    AlchemyAsyncRequest,
    AlchemyAsyncRequestFormItem,
    AlchemyAsyncResponse,
)
from horde_sdk.ai_horde_api.apimodels.alchemy._pop import (
    AlchemyFormPayloadStable,
    AlchemyPopFormPayload,
    AlchemyPopRequest,
    AlchemyPopResponse,
    NoValidAlchemyFound,
)
from horde_sdk.ai_horde_api.apimodels.alchemy._status import (
    AlchemyCaptionResult,
    AlchemyDeleteRequest,
    AlchemyFormStatus,
    AlchemyInterrogationDetails,
    AlchemyInterrogationResult,
    AlchemyInterrogationResultItem,
    AlchemyNSFWResult,
    AlchemyStatusRequest,
    AlchemyStatusResponse,
    AlchemyUpscaleResult,
)
from horde_sdk.ai_horde_api.apimodels.alchemy._submit import AlchemyJobSubmitRequest, AlchemyJobSubmitResponse
from horde_sdk.ai_horde_api.apimodels.base import (
    ExtraSourceImageEntry,
    ExtraTextEntry,
    GenMetadataEntry,
    ImageGenerateParamMixin,
    JobRequestMixin,
    JobResponseMixin,
    JobSubmitResponse,
    LorasPayloadEntry,
    SingleWarningEntry,
    TIPayloadEntry,
    WorkerRequestMixin,
    WorkerRequestNameMixin,
)
from horde_sdk.ai_horde_api.apimodels.generate._async import (
    ImageGenerateAsyncDryRunResponse,
    ImageGenerateAsyncRequest,
    ImageGenerateAsyncResponse,
    ImageGenerationInputPayload,
)
from horde_sdk.ai_horde_api.apimodels.generate._check import ImageGenerateCheckRequest, ImageGenerateCheckResponse
from horde_sdk.ai_horde_api.apimodels.generate._pop import (
    ImageGenerateJobPopPayload,
    ImageGenerateJobPopRequest,
    ImageGenerateJobPopResponse,
    ImageGenerateJobPopSkippedStatus,
    PopInput,
)
from horde_sdk.ai_horde_api.apimodels.generate._progress import (
    ResponseGenerationProgressCombinedMixin,
    ResponseGenerationProgressInfoMixin,
)
from horde_sdk.ai_horde_api.apimodels.generate._status import (
    DeleteImageGenerateRequest,
    ImageGenerateStatusRequest,
    ImageGenerateStatusResponse,
    ImageGeneration,
)
from horde_sdk.ai_horde_api.apimodels.generate._submit import (
    ImageGenerationJobSubmitRequest,
)
from horde_sdk.ai_horde_api.apimodels.generate.text._async import (
    ModelGenerationInputKobold,
    ModelPayloadRootKobold,
    TextGenerateAsyncDryRunResponse,
    TextGenerateAsyncRequest,
    TextGenerateAsyncResponse,
)
from horde_sdk.ai_horde_api.apimodels.generate.text._pop import (
    ModelPayloadKobold,
    NoValidRequestFoundKobold,
    TextGenerateJobPopRequest,
    TextGenerateJobPopResponse,
    _PopInputKobold,
)
from horde_sdk.ai_horde_api.apimodels.generate.text._status import (
    DeleteTextGenerateRequest,
    GenerationKobold,
    TextGenerateStatusRequest,
    TextGenerateStatusResponse,
)
from horde_sdk.ai_horde_api.apimodels.generate.text._submit import (
    TextGenerationJobSubmitRequest,
)
from horde_sdk.ai_horde_api.apimodels.workers._workers import (
    AllWorkersDetailsRequest,
    AllWorkersDetailsResponse,
    DeleteWorkerRequest,
    DeleteWorkerResponse,
    ModifyWorkerRequest,
    ModifyWorkerResponse,
    SingleWorkerDetailsRequest,
    SingleWorkerDetailsResponse,
    SingleWorkerNameDetailsRequest,
    TeamDetailsLite,
    WorkerDetailItem,
    WorkerKudosDetails,
)
from horde_sdk.ai_horde_api.consts import KNOWN_ALCHEMY_TYPES
from horde_sdk.generic_api.apimodels import (
    APIKeyAllowedInRequestMixin,
    ContainsMessageResponseMixin,
    MessageSpecifiesUserIDMixin,
    RequestUsesWorkerMixin,
    ResponseRequiringDownloadMixin,
    ResponseRequiringFollowUpMixin,
    ResponseWithProgressMixin,
)

__all__ = [
    "AIHordeDocumentRequestMixin",
    "AIHordeGetPrivacyPolicyRequest",
    "AIHordeGetSponsorsRequest",
    "AIHordeGetTermsRequest",
    "DocumentFormat",
    "HordeDocument",
    "ActiveGenerations",
    "ContributionsDetails",
    "FindUserRequest",
    "KudosTransferRequest",
    "KudosTransferResponse",
    "UserDetailsResponse",
    "MonthlyKudos",
    "UsageDetails",
    "UserAmountRecords",
    "UserKudosDetails",
    "UserRecords",
    "UserThingRecords",
    "_ModifyUserBase",
    "ImageStatsModelsRequest",
    "ImageStatsModelsTotalRequest",
    "ImageStatsModelsTotalResponse",
    "HordeModes",
    "HordePerformanceRequest",
    "HordePerformanceResponse",
    "HordeStatusModelsAllRequest",
    "HordeStatusModelsAllResponse",
    "HordeStatusModelsSingleRequest",
    "HordeStatusModelsSingleResponse",
    "Newspiece",
    "NewsRequest",
    "NewsResponse",
    "ResponseModelStylesUser",
    "ListUsersDetailsRequest",
    "ListUsersDetailsResponse",
    "ModifyUser",
    "ModifyUserReply",
    "SingleUserDetailsRequest",
    "ModifyUserRequest",
    "ModifyUserResponse",
    "ActiveModel",
    "ActiveModelLite",
    "SinglePeriodImgStat",
    "SinglePeriodTxtStat",
    "ImageStatsModelsResponse",
    "StatsModelsTimeframe",
    "TextStatsModelResponse",
    "TextStatsModelsRequest",
    "TextStatsModelsTotalRequest",
    "TextStatsModelsTotalResponse",
    "AIHordeHeartbeatRequest",
    "AIHordeHeartbeatResponse",
    "KNOWN_ALCHEMY_TYPES",
    "AlchemyAsyncRequest",
    "AlchemyAsyncRequestFormItem",
    "AlchemyAsyncResponse",
    "AlchemyFormPayloadStable",
    "AlchemyPopFormPayload",
    "AlchemyPopRequest",
    "AlchemyPopResponse",
    "NoValidAlchemyFound",
    "AlchemyCaptionResult",
    "AlchemyDeleteRequest",
    "AlchemyFormStatus",
    "AlchemyInterrogationDetails",
    "AlchemyInterrogationResult",
    "AlchemyInterrogationResultItem",
    "AlchemyNSFWResult",
    "AlchemyStatusRequest",
    "AlchemyStatusResponse",
    "AlchemyUpscaleResult",
    "AlchemyJobSubmitRequest",
    "AlchemyJobSubmitResponse",
    "ExtraSourceImageEntry",
    "ExtraTextEntry",
    "GenMetadataEntry",
    "ImageGenerateParamMixin",
    "JobRequestMixin",
    "JobResponseMixin",
    "LorasPayloadEntry",
    "SingleWarningEntry",
    "TIPayloadEntry",
    "WorkerRequestMixin",
    "WorkerRequestNameMixin",
    "ImageGenerateAsyncDryRunResponse",
    "ImageGenerateAsyncRequest",
    "ImageGenerateAsyncResponse",
    "ImageGenerationInputPayload",
    "ImageGenerateCheckRequest",
    "ImageGenerateCheckResponse",
    "ImageGenerateJobPopPayload",
    "ImageGenerateJobPopRequest",
    "ImageGenerateJobPopResponse",
    "ImageGenerateJobPopSkippedStatus",
    "PopInput",
    "ResponseGenerationProgressCombinedMixin",
    "ResponseGenerationProgressInfoMixin",
    "DeleteImageGenerateRequest",
    "ImageGenerateStatusRequest",
    "ImageGenerateStatusResponse",
    "ImageGeneration",
    "ImageGenerationJobSubmitRequest",
    "JobSubmitResponse",
    "ModelGenerationInputKobold",
    "ModelPayloadRootKobold",
    "TextGenerateAsyncRequest",
    "TextGenerateAsyncResponse",
    "ModelPayloadKobold",
    "NoValidRequestFoundKobold",
    "TextGenerateJobPopRequest",
    "TextGenerateJobPopResponse",
    "_PopInputKobold",
    "TextGenerateAsyncDryRunResponse",
    "DeleteTextGenerateRequest",
    "GenerationKobold",
    "TextGenerateStatusRequest",
    "TextGenerateStatusResponse",
    "TextGenerationJobSubmitRequest",
    "AllWorkersDetailsRequest",
    "AllWorkersDetailsResponse",
    "DeleteWorkerRequest",
    "DeleteWorkerResponse",
    "ModifyWorkerResponse",
    "ModifyWorkerRequest",
    "SingleWorkerNameDetailsRequest",
    "SingleWorkerDetailsRequest",
    "SingleWorkerDetailsResponse",
    "TeamDetailsLite",
    "WorkerDetailItem",
    "WorkerKudosDetails",
    "APIKeyAllowedInRequestMixin",
    "ContainsMessageResponseMixin",
    "MessageSpecifiesUserIDMixin",
    "RequestUsesWorkerMixin",
    "ResponseRequiringDownloadMixin",
    "ResponseRequiringFollowUpMixin",
    "ResponseWithProgressMixin",
]
