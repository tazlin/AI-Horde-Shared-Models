"""All requests, responses and API models defined for the AI Horde API."""

from horde_sdk.ai_horde_api.apimodels._find_user import (
    ContributionsDetails,
    FindUserRequest,
    FindUserResponse,
    MonthlyKudos,
    UsageDetails,
    UserAmountRecords,
    UserKudosDetails,
    UserRecords,
    UserThingRecords,
)
from horde_sdk.ai_horde_api.apimodels._stats import (
    ImageModelStatsResponse,
    ImageStatsModelsRequest,
    ImageStatsModelsTotalRequest,
    ImageStatsModelsTotalResponse,
    SinglePeriodImgStat,
    SinglePeriodTxtStat,
    StatsModelsTimeframe,
    TextModelStatsResponse,
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
    ModifyWorker,
    ModifyWorkerInput,
    SingleWorkerDetailsRequest,
    SingleWorkerDetailsResponse,
    TeamDetailsLite,
    WorkerDetailItem,
    WorkerKudosDetails,
)
from horde_sdk.ai_horde_api.consts import KNOWN_ALCHEMY_TYPES
from horde_sdk.generic_api.apimodels import (
    APIKeyAllowedInRequestMixin,
    ContainsMessageResponseMixin,
    RequestSpecifiesUserIDMixin,
    RequestUsesWorkerMixin,
    ResponseRequiringDownloadMixin,
    ResponseRequiringFollowUpMixin,
    ResponseWithProgressMixin,
)

__all__ = [
    "ContributionsDetails",
    "FindUserRequest",
    "FindUserResponse",
    "MonthlyKudos",
    "UsageDetails",
    "UserAmountRecords",
    "UserKudosDetails",
    "UserRecords",
    "UserThingRecords",
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
    "ActiveModel",
    "ActiveModelLite",
    "SinglePeriodImgStat",
    "SinglePeriodTxtStat",
    "ImageModelStatsResponse",
    "StatsModelsTimeframe",
    "TextModelStatsResponse",
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
    "ModifyWorker",
    "ModifyWorkerInput",
    "SingleWorkerDetailsRequest",
    "SingleWorkerDetailsResponse",
    "TeamDetailsLite",
    "WorkerDetailItem",
    "WorkerKudosDetails",
    "APIKeyAllowedInRequestMixin",
    "ContainsMessageResponseMixin",
    "RequestSpecifiesUserIDMixin",
    "RequestUsesWorkerMixin",
    "ResponseRequiringDownloadMixin",
    "ResponseRequiringFollowUpMixin",
    "ResponseWithProgressMixin",
]
