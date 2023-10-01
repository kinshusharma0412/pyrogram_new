# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

count = 459

exceptions = {
    420: {
        "_": "Flood",
        "2FA_CONFIRM_WAIT_X": "TwoFaConfirmWait",
        "FLOOD_TEST_PHONE_WAIT_X": "FloodTestPhoneWait",
        "FLOOD_WAIT_X": "FloodWait",
        "SLOWMODE_WAIT_X": "SlowmodeWait",
        "TAKEOUT_INIT_DELAY_X": "TakeoutInitDelay",
    },
    401: {
        "_": "Unauthorized",
        "ACTIVE_USER_REQUIRED": "ActiveUserRequired",
        "AUTH_KEY_INVALID": "AuthKeyInvalid",
        "AUTH_KEY_PERM_EMPTY": "AuthKeyPermEmpty",
        "AUTH_KEY_UNREGISTERED": "AuthKeyUnregistered",
        "SESSION_EXPIRED": "SessionExpired",
        "SESSION_PASSWORD_NEEDED": "SessionPasswordNeeded",
        "SESSION_REVOKED": "SessionRevoked",
        "USER_DEACTIVATED": "UserDeactivated",
        "USER_DEACTIVATED_BAN": "UserDeactivatedBan",
    },
    403: {
        "_": "Forbidden",
        "BROADCAST_FORBIDDEN": "BroadcastForbidden",
        "CHANNEL_PUBLIC_GROUP_NA": "ChannelPublicGroupNa",
        "CHAT_ADMIN_INVITE_REQUIRED": "ChatAdminInviteRequired",
        "CHAT_ADMIN_REQUIRED": "ChatAdminRequired",
        "CHAT_FORBIDDEN": "ChatForbidden",
        "CHAT_SEND_GIFS_FORBIDDEN": "ChatSendGifsForbidden",
        "CHAT_SEND_INLINE_FORBIDDEN": "ChatSendInlineForbidden",
        "CHAT_SEND_MEDIA_FORBIDDEN": "ChatSendMediaForbidden",
        "CHAT_SEND_POLL_FORBIDDEN": "ChatSendPollForbidden",
        "CHAT_SEND_STICKERS_FORBIDDEN": "ChatSendStickersForbidden",
        "CHAT_WRITE_FORBIDDEN": "ChatWriteForbidden",
        "EDIT_BOT_INVITE_FORBIDDEN": "EditBotInviteForbidden",
        "INLINE_BOT_REQUIRED": "InlineBotRequired",
        "MESSAGE_AUTHOR_REQUIRED": "MessageAuthorRequired",
        "MESSAGE_DELETE_FORBIDDEN": "MessageDeleteForbidden",
        "POLL_VOTE_REQUIRED": "PollVoteRequired",
        "RIGHT_FORBIDDEN": "RightForbidden",
        "SENSITIVE_CHANGE_FORBIDDEN": "SensitiveChangeForbidden",
        "TAKEOUT_REQUIRED": "TakeoutRequired",
        "USER_BOT_INVALID": "UserBotInvalid",
        "USER_CHANNELS_TOO_MUCH": "UserChannelsTooMuch",
        "USER_INVALID": "UserInvalid",
        "USER_IS_BLOCKED": "UserIsBlocked",
        "USER_NOT_MUTUAL_CONTACT": "UserNotMutualContact",
        "USER_PRIVACY_RESTRICTED": "UserPrivacyRestricted",
        "USER_RESTRICTED": "UserRestricted",
        "PREMIUM_ACCOUNT_REQUIRED": "PremiumAccountRequired",
    },
    400: {
        "_": "BadRequest",
        "ABOUT_TOO_LONG": "AboutTooLong",
        "ACCESS_TOKEN_EXPIRED": "AccessTokenExpired",
        "ACCESS_TOKEN_INVALID": "AccessTokenInvalid",
        "ADMINS_TOO_MUCH": "AdminsTooMuch",
        "ADMIN_RANK_EMOJI_NOT_ALLOWED": "AdminRankEmojiNotAllowed",
        "ADMIN_RANK_INVALID": "AdminRankInvalid",
        "ALBUM_PHOTOS_TOO_MANY": "AlbumPhotosTooMany",
        "API_ID_INVALID": "ApiIdInvalid",
        "API_ID_PUBLISHED_FLOOD": "ApiIdPublishedFlood",
        "ARTICLE_TITLE_EMPTY": "ArticleTitleEmpty",
        "AUDIO_TITLE_EMPTY": "AudioTitleEmpty",
        "AUTH_BYTES_INVALID": "AuthBytesInvalid",
        "AUTH_TOKEN_ALREADY_ACCEPTED": "AuthTokenAlreadyAccepted",
        "AUTH_TOKEN_EXPIRED": "AuthTokenExpired",
        "AUTH_TOKEN_INVALID": "AuthTokenInvalid",
        "AUTOARCHIVE_NOT_AVAILABLE": "AutoarchiveNotAvailable",
        "BANK_CARD_NUMBER_INVALID": "BankCardNumberInvalid",
        "BANNED_RIGHTS_INVALID": "BannedRightsInvalid",
        "BASE_PORT_LOC_INVALID": "BasePortLocInvalid",
        "BOTS_TOO_MUCH": "BotsTooMuch",
        "BOT_CHANNELS_NA": "BotChannelsNa",
        "BOT_COMMAND_DESCRIPTION_INVALID": "BotCommandDescriptionInvalid",
        "BOT_DOMAIN_INVALID": "BotDomainInvalid",
        "BOT_GAMES_DISABLED": "BotGamesDisabled",
        "BOT_GROUPS_BLOCKED": "BotGroupsBlocked",
        "BOT_INLINE_DISABLED": "BotInlineDisabled",
        "BOT_INVALID": "BotInvalid",
        "BOT_METHOD_INVALID": "BotMethodInvalid",
        "BOT_MISSING": "BotMissing",
        "BOT_PAYMENTS_DISABLED": "BotPaymentsDisabled",
        "BOT_POLLS_DISABLED": "BotPollsDisabled",
        "BOT_RESPONSE_TIMEOUT": "BotResponseTimeout",
        "BOT_SCORE_NOT_MODIFIED": "BotScoreNotModified",
        "BROADCAST_ID_INVALID": "BroadcastIdInvalid",
        "BROADCAST_PUBLIC_VOTERS_FORBIDDEN": "BroadcastPublicVotersForbidden",
        "BROADCAST_REQUIRED": "BroadcastRequired",
        "BUTTON_DATA_INVALID": "ButtonDataInvalid",
        "BUTTON_TYPE_INVALID": "ButtonTypeInvalid",
        "BUTTON_URL_INVALID": "ButtonUrlInvalid",
        "CALL_ALREADY_ACCEPTED": "CallAlreadyAccepted",
        "CALL_ALREADY_DECLINED": "CallAlreadyDeclined",
        "CALL_PEER_INVALID": "CallPeerInvalid",
        "CALL_PROTOCOL_FLAGS_INVALID": "CallProtocolFlagsInvalid",
        "CDN_METHOD_INVALID": "CdnMethodInvalid",
        "CHANNELS_ADMIN_PUBLIC_TOO_MUCH": "ChannelsAdminPublicTooMuch",
        "CHANNELS_TOO_MUCH": "ChannelsTooMuch",
        "CHANNEL_ADD_INVALID": "ChannelAddInvalid",
        "CHANNEL_BANNED": "ChannelBanned",
        "CHANNEL_INVALID": "ChannelInvalid",
        "CHANNEL_PRIVATE": "ChannelPrivate",
        "CHANNEL_TOO_LARGE": "ChannelTooLarge",
        "CHAT_ABOUT_NOT_MODIFIED": "ChatAboutNotModified",
        "CHAT_ABOUT_TOO_LONG": "ChatAboutTooLong",
        "CHAT_ADMIN_REQUIRED": "ChatAdminRequired",
        "CHAT_FORWARDS_RESTRICTED": "ChatForwardsRestricted",
        "CHAT_ID_EMPTY": "ChatIdEmpty",
        "CHAT_ID_INVALID": "ChatIdInvalid",
        "CHAT_INVALID": "ChatInvalid",
        "CHAT_INVITE_PERMANENT": "ChatInvitePermanent",
        "CHAT_LINK_EXISTS": "ChatLinkExists",
        "CHAT_NOT_MODIFIED": "ChatNotModified",
        "CHAT_RESTRICTED": "ChatRestricted",
        "CHAT_SEND_INLINE_FORBIDDEN": "ChatSendInlineForbidden",
        "CHAT_TITLE_EMPTY": "ChatTitleEmpty",
        "CHAT_TOO_BIG": "ChatTooBig",
        "CODE_EMPTY": "CodeEmpty",
        "CODE_HASH_INVALID": "CodeHashInvalid",
        "CODE_INVALID": "CodeInvalid",
        "CONNECTION_API_ID_INVALID": "ConnectionApiIdInvalid",
        "CONNECTION_APP_VERSION_EMPTY": "ConnectionAppVersionEmpty",
        "CONNECTION_DEVICE_MODEL_EMPTY": "ConnectionDeviceModelEmpty",
        "CONNECTION_LANG_PACK_INVALID": "ConnectionLangPackInvalid",
        "CONNECTION_LAYER_INVALID": "ConnectionLayerInvalid",
        "CONNECTION_NOT_INITED": "ConnectionNotInited",
        "CONNECTION_SYSTEM_EMPTY": "ConnectionSystemEmpty",
        "CONNECTION_SYSTEM_LANG_CODE_EMPTY": "ConnectionSystemLangCodeEmpty",
        "CONTACT_ADD_MISSING": "ContactAddMissing",
        "CONTACT_ID_INVALID": "ContactIdInvalid",
        "CONTACT_NAME_EMPTY": "ContactNameEmpty",
        "CONTACT_REQ_MISSING": "ContactReqMissing",
        "DATA_INVALID": "DataInvalid",
        "DATA_JSON_INVALID": "DataJsonInvalid",
        "DATA_TOO_LONG": "DataTooLong",
        "DATE_EMPTY": "DateEmpty",
        "DC_ID_INVALID": "DcIdInvalid",
        "DH_G_A_INVALID": "DhGAInvalid",
        "DOCUMENT_INVALID": "DocumentInvalid",
        "EMAIL_HASH_EXPIRED": "EmailHashExpired",
        "EMAIL_INVALID": "EmailInvalid",
        "EMAIL_UNCONFIRMED": "EmailUnconfirmed",
        "EMAIL_UNCONFIRMED_X": "EmailUnconfirmed",
        "EMAIL_VERIFY_EXPIRED": "EmailVerifyExpired",
        "EMOTICON_EMPTY": "EmoticonEmpty",
        "EMOTICON_INVALID": "EmoticonInvalid",
        "EMOTICON_STICKERPACK_MISSING": "EmoticonStickerpackMissing",
        "ENCRYPTED_MESSAGE_INVALID": "EncryptedMessageInvalid",
        "ENCRYPTION_ALREADY_ACCEPTED": "EncryptionAlreadyAccepted",
        "ENCRYPTION_ALREADY_DECLINED": "EncryptionAlreadyDeclined",
        "ENCRYPTION_DECLINED": "EncryptionDeclined",
        "ENCRYPTION_ID_INVALID": "EncryptionIdInvalid",
        "ENTITIES_TOO_LONG": "EntitiesTooLong",
        "ENTITY_MENTION_USER_INVALID": "EntityMentionUserInvalid",
        "ERROR_TEXT_EMPTY": "ErrorTextEmpty",
        "EXPIRE_DATE_INVALID": "ExpireDateInvalid",
        "EXPORT_CARD_INVALID": "ExportCardInvalid",
        "EXTERNAL_URL_INVALID": "ExternalUrlInvalid",
        "FIELD_NAME_EMPTY": "FieldNameEmpty",
        "FIELD_NAME_INVALID": "FieldNameInvalid",
        "FILE_ID_INVALID": "FileIdInvalid",
        "FILE_MIGRATE_X": "FileMigrate",
        "FILE_PARTS_INVALID": "FilePartsInvalid",
        "FILE_PART_EMPTY": "FilePartEmpty",
        "FILE_PART_INVALID": "FilePartInvalid",
        "FILE_PART_LENGTH_INVALID": "FilePartLengthInvalid",
        "FILE_PART_SIZE_CHANGED": "FilePartSizeChanged",
        "FILE_PART_SIZE_INVALID": "FilePartSizeInvalid",
        "FILE_PART_TOO_BIG": "FilePartTooBig",
        "FILE_PART_X_MISSING": "FilePartMissing",
        "FILE_REFERENCE_EMPTY": "FileReferenceEmpty",
        "FILE_REFERENCE_EXPIRED": "FileReferenceExpired",
        "FILE_REFERENCE_INVALID": "FileReferenceInvalid",
        "FILTER_ID_INVALID": "FilterIdInvalid",
        "FIRSTNAME_INVALID": "FirstnameInvalid",
        "FOLDER_ID_EMPTY": "FolderIdEmpty",
        "FOLDER_ID_INVALID": "FolderIdInvalid",
        "FRESH_CHANGE_ADMINS_FORBIDDEN": "FreshChangeAdminsForbidden",
        "FROM_MESSAGE_BOT_DISABLED": "FromMessageBotDisabled",
        "FROM_PEER_INVALID": "FromPeerInvalid",
        "GAME_BOT_INVALID": "GameBotInvalid",
        "GEO_POINT_INVALID": "GeoPointInvalid",
        "GIF_CONTENT_TYPE_INVALID": "GifContentTypeInvalid",
        "GIF_ID_INVALID": "GifIdInvalid",
        "GRAPH_INVALID_RELOAD": "GraphInvalidReload",
        "GRAPH_OUTDATED_RELOAD": "GraphOutdatedReload",
        "GROUPCALL_SSRC_DUPLICATE_MUCH": "GroupcallSsrcDuplicateMuch",
        "GROUPED_MEDIA_INVALID": "GroupedMediaInvalid",
        "GROUP_CALL_INVALID": "GroupCallInvalid",
        "HASH_INVALID": "HashInvalid",
        "IMAGE_PROCESS_FAILED": "ImageProcessFailed",
        "IMPORT_FILE_INVALID": "ImportFileInvalid",
        "IMPORT_FORMAT_UNRECOGNIZED": "ImportFormatUnrecognized",
        "IMPORT_ID_INVALID": "ImportIdInvalid",
        "INLINE_RESULT_EXPIRED": "InlineResultExpired",
        "INPUT_CONSTRUCTOR_INVALID": "InputConstructorInvalid",
        "INPUT_FETCH_ERROR": "InputFetchError",
        "INPUT_FETCH_FAIL": "InputFetchFail",
        "INPUT_FILTER_INVALID": "InputFilterInvalid",
        "INPUT_LAYER_INVALID": "InputLayerInvalid",
        "INPUT_METHOD_INVALID": "InputMethodInvalid",
        "INPUT_REQUEST_TOO_LONG": "InputRequestTooLong",
        "INPUT_USER_DEACTIVATED": "InputUserDeactivated",
        "INVITE_HASH_EMPTY": "InviteHashEmpty",
        "INVITE_HASH_EXPIRED": "InviteHashExpired",
        "INVITE_HASH_INVALID": "InviteHashInvalid",
        "INVITE_REVOKED_MISSING": "InviteRevokedMissing",
        "LANG_PACK_INVALID": "LangPackInvalid",
        "LASTNAME_INVALID": "LastnameInvalid",
        "LIMIT_INVALID": "LimitInvalid",
        "LINK_NOT_MODIFIED": "LinkNotModified",
        "LOCATION_INVALID": "LocationInvalid",
        "MAX_ID_INVALID": "MaxIdInvalid",
        "MAX_QTS_INVALID": "MaxQtsInvalid",
        "MD5_CHECKSUM_INVALID": "Md5ChecksumInvalid",
        "MEDIA_CAPTION_TOO_LONG": "MediaCaptionTooLong",
        "MEDIA_EMPTY": "MediaEmpty",
        "MEDIA_INVALID": "MediaInvalid",
        "MEDIA_NEW_INVALID": "MediaNewInvalid",
        "MEDIA_PREV_INVALID": "MediaPrevInvalid",
        "MEGAGROUP_ID_INVALID": "MegagroupIdInvalid",
        "MEGAGROUP_PREHISTORY_HIDDEN": "MegagroupPrehistoryHidden",
        "MEGAGROUP_REQUIRED": "MegagroupRequired",
        "MESSAGE_EDIT_TIME_EXPIRED": "MessageEditTimeExpired",
        "MESSAGE_EMPTY": "MessageEmpty",
        "MESSAGE_IDS_EMPTY": "MessageIdsEmpty",
        "MESSAGE_ID_INVALID": "MessageIdInvalid",
        "MESSAGE_NOT_MODIFIED": "MessageNotModified",
        "MESSAGE_POLL_CLOSED": "MessagePollClosed",
        "MESSAGE_TOO_LONG": "MessageTooLong",
        "METHOD_INVALID": "MethodInvalid",
        "MSG_ID_INVALID": "MsgIdInvalid",
        "MSG_WAIT_FAILED": "MsgWaitFailed",
        "MULTI_MEDIA_TOO_LONG": "MultiMediaTooLong",
        "NEW_SALT_INVALID": "NewSaltInvalid",
        "NEW_SETTINGS_INVALID": "NewSettingsInvalid",
        "NEXT_OFFSET_INVALID": "NextOffsetInvalid",
        "OFFSET_INVALID": "OffsetInvalid",
        "OFFSET_PEER_ID_INVALID": "OffsetPeerIdInvalid",
        "OPTIONS_TOO_MUCH": "OptionsTooMuch",
        "OPTION_INVALID": "OptionInvalid",
        "PACK_SHORT_NAME_INVALID": "PackShortNameInvalid",
        "PACK_SHORT_NAME_OCCUPIED": "PackShortNameOccupied",
        "PACK_TITLE_INVALID": "PackTitleInvalid",
        "PARTICIPANTS_TOO_FEW": "ParticipantsTooFew",
        "PARTICIPANT_VERSION_OUTDATED": "ParticipantVersionOutdated",
        "PASSWORD_EMPTY": "PasswordEmpty",
        "PASSWORD_HASH_INVALID": "PasswordHashInvalid",
        "PASSWORD_MISSING": "PasswordMissing",
        "PASSWORD_RECOVERY_NA": "PasswordRecoveryNa",
        "PASSWORD_REQUIRED": "PasswordRequired",
        "PASSWORD_TOO_FRESH_X": "PasswordTooFresh",
        "PAYMENT_PROVIDER_INVALID": "PaymentProviderInvalid",
        "PEER_FLOOD": "PeerFlood",
        "PEER_ID_INVALID": "PeerIdInvalid",
        "PEER_ID_NOT_SUPPORTED": "PeerIdNotSupported",
        "PERSISTENT_TIMESTAMP_EMPTY": "PersistentTimestampEmpty",
        "PERSISTENT_TIMESTAMP_INVALID": "PersistentTimestampInvalid",
        "PHONE_CODE_EMPTY": "PhoneCodeEmpty",
        "PHONE_CODE_EXPIRED": "PhoneCodeExpired",
        "PHONE_CODE_HASH_EMPTY": "PhoneCodeHashEmpty",
        "PHONE_CODE_INVALID": "PhoneCodeInvalid",
        "PHONE_NUMBER_APP_SIGNUP_FORBIDDEN": "PhoneNumberAppSignupForbidden",
        "PHONE_NUMBER_BANNED": "PhoneNumberBanned",
        "PHONE_NUMBER_FLOOD": "PhoneNumberFlood",
        "PHONE_NUMBER_INVALID": "PhoneNumberInvalid",
        "PHONE_NUMBER_OCCUPIED": "PhoneNumberOccupied",
        "PHONE_NUMBER_UNOCCUPIED": "PhoneNumberUnoccupied",
        "PHONE_PASSWORD_PROTECTED": "PhonePasswordProtected",
        "PHOTO_CONTENT_TYPE_INVALID": "PhotoContentTypeInvalid",
        "PHOTO_CONTENT_URL_EMPTY": "PhotoContentUrlEmpty",
        "PHOTO_CROP_FILE_MISSING": "PhotoCropFileMissing",
        "PHOTO_CROP_SIZE_SMALL": "PhotoCropSizeSmall",
        "PHOTO_EXT_INVALID": "PhotoExtInvalid",
        "PHOTO_FILE_MISSING": "PhotoFileMissing",
        "PHOTO_ID_INVALID": "PhotoIdInvalid",
        "PHOTO_INVALID": "PhotoInvalid",
        "PHOTO_INVALID_DIMENSIONS": "PhotoInvalidDimensions",
        "PHOTO_SAVE_FILE_INVALID": "PhotoSaveFileInvalid",
        "PHOTO_THUMB_URL_EMPTY": "PhotoThumbUrlEmpty",
        "PHOTO_THUMB_URL_INVALID": "PhotoThumbUrlInvalid",
        "PINNED_DIALOGS_TOO_MUCH": "PinnedDialogsTooMuch",
        "PIN_RESTRICTED": "PinRestricted",
        "POLL_ANSWERS_INVALID": "PollAnswersInvalid",
        "POLL_OPTION_DUPLICATE": "PollOptionDuplicate",
        "POLL_OPTION_INVALID": "PollOptionInvalid",
        "POLL_QUESTION_INVALID": "PollQuestionInvalid",
        "POLL_UNSUPPORTED": "PollUnsupported",
        "POLL_VOTE_REQUIRED": "PollVoteRequired",
        "PRIVACY_KEY_INVALID": "PrivacyKeyInvalid",
        "PRIVACY_TOO_LONG": "PrivacyTooLong",
        "PRIVACY_VALUE_INVALID": "PrivacyValueInvalid",
        "QUERY_ID_EMPTY": "QueryIdEmpty",
        "QUERY_ID_INVALID": "QueryIdInvalid",
        "QUERY_TOO_SHORT": "QueryTooShort",
        "QUIZ_CORRECT_ANSWERS_EMPTY": "QuizCorrectAnswersEmpty",
        "QUIZ_CORRECT_ANSWERS_TOO_MUCH": "QuizCorrectAnswersTooMuch",
        "QUIZ_CORRECT_ANSWER_INVALID": "QuizCorrectAnswerInvalid",
        "QUIZ_MULTIPLE_INVALID": "QuizMultipleInvalid",
        "RANDOM_ID_EMPTY": "RandomIdEmpty",
        "RANDOM_ID_INVALID": "RandomIdInvalid",
        "RANDOM_LENGTH_INVALID": "RandomLengthInvalid",
        "RANGES_INVALID": "RangesInvalid",
        "REACTION_EMPTY": "ReactionEmpty",
        "REACTION_INVALID": "ReactionInvalid",
        "REFLECTOR_NOT_AVAILABLE": "ReflectorNotAvailable",
        "REPLY_MARKUP_BUY_EMPTY": "ReplyMarkupBuyEmpty",
        "REPLY_MARKUP_GAME_EMPTY": "ReplyMarkupGameEmpty",
        "REPLY_MARKUP_INVALID": "ReplyMarkupInvalid",
        "REPLY_MARKUP_TOO_LONG": "ReplyMarkupTooLong",
        "RESULTS_TOO_MUCH": "ResultsTooMuch",
        "RESULT_ID_DUPLICATE": "ResultIdDuplicate",
        "RESULT_ID_EMPTY": "ResultIdEmpty",
        "RESULT_ID_INVALID": "ResultIdInvalid",
        "RESULT_TYPE_INVALID": "ResultTypeInvalid",
        "REVOTE_NOT_ALLOWED": "RevoteNotAllowed",
        "RSA_DECRYPT_FAILED": "RsaDecryptFailed",
        "SCHEDULE_BOT_NOT_ALLOWED": "ScheduleBotNotAllowed",
        "SCHEDULE_DATE_INVALID": "ScheduleDateInvalid",
        "SCHEDULE_DATE_TOO_LATE": "ScheduleDateTooLate",
        "SCHEDULE_STATUS_PRIVATE": "ScheduleStatusPrivate",
        "SCHEDULE_TOO_MUCH": "ScheduleTooMuch",
        "SEARCH_QUERY_EMPTY": "SearchQueryEmpty",
        "SECONDS_INVALID": "SecondsInvalid",
        "SEND_MESSAGE_MEDIA_INVALID": "SendMessageMediaInvalid",
        "SEND_MESSAGE_TYPE_INVALID": "SendMessageTypeInvalid",
        "SESSION_TOO_FRESH_X": "SessionTooFresh",
        "SETTINGS_INVALID": "SettingsInvalid",
        "SHA256_HASH_INVALID": "Sha256HashInvalid",
        "SHORTNAME_OCCUPY_FAILED": "ShortnameOccupyFailed",
        "SLOWMODE_MULTI_MSGS_DISABLED": "SlowmodeMultiMsgsDisabled",
        "SMS_CODE_CREATE_FAILED": "SmsCodeCreateFailed",
        "SRP_ID_INVALID": "SrpIdInvalid",
        "SRP_PASSWORD_CHANGED": "SrpPasswordChanged",
        "START_PARAM_EMPTY": "StartParamEmpty",
        "START_PARAM_INVALID": "StartParamInvalid",
        "START_PARAM_TOO_LONG": "StartParamTooLong",
        "STICKERSET_INVALID": "StickersetInvalid",
        "STICKERSET_NOT_MODIFIED": "StickersetNotModified",
        "STICKERS_EMPTY": "StickersEmpty",
        "STICKERS_TOO_MUCH": "StickersTooMuch",
        "STICKER_DOCUMENT_INVALID": "StickerDocumentInvalid",
        "STICKER_EMOJI_INVALID": "StickerEmojiInvalid",
        "STICKER_FILE_INVALID": "StickerFileInvalid",
        "STICKER_ID_INVALID": "StickerIdInvalid",
        "STICKER_INVALID": "StickerInvalid",
        "STICKER_PNG_DIMENSIONS": "StickerPngDimensions",
        "STICKER_PNG_NOPNG": "StickerPngNopng",
        "STICKER_TGS_NOTGS": "StickerTgsNotgs",
        "STICKER_VIDEO_NOWEBM": "StickerVideoNowebm",
        "STICKER_THUMB_PNG_NOPNG": "StickerThumbPngNopng",
        "TAKEOUT_INVALID": "TakeoutInvalid",
        "TAKEOUT_REQUIRED": "TakeoutRequired",
        "TEMP_AUTH_KEY_EMPTY": "TempAuthKeyEmpty",
        "THEME_FILE_INVALID": "ThemeFileInvalid",
        "THEME_FORMAT_INVALID": "ThemeFormatInvalid",
        "THEME_INVALID": "ThemeInvalid",
        "THEME_MIME_INVALID": "ThemeMimeInvalid",
        "TMP_PASSWORD_DISABLED": "TmpPasswordDisabled",
        "TMP_PASSWORD_INVALID": "TmpPasswordInvalid",
        "TOKEN_INVALID": "TokenInvalid",
        "TTL_DAYS_INVALID": "TtlDaysInvalid",
        "TTL_MEDIA_INVALID": "TtlMediaInvalid",
        "TYPES_EMPTY": "TypesEmpty",
        "TYPE_CONSTRUCTOR_INVALID": "TypeConstructorInvalid",
        "UNTIL_DATE_INVALID": "UntilDateInvalid",
        "URL_INVALID": "UrlInvalid",
        "USAGE_LIMIT_INVALID": "UsageLimitInvalid",
        "USERNAME_INVALID": "UsernameInvalid",
        "USERNAME_NOT_MODIFIED": "UsernameNotModified",
        "USERNAME_NOT_OCCUPIED": "UsernameNotOccupied",
        "USERNAME_OCCUPIED": "UsernameOccupied",
        "USERPIC_UPLOAD_REQUIRED": "UserpicUploadRequired",
        "USERS_TOO_FEW": "UsersTooFew",
        "USERS_TOO_MUCH": "UsersTooMuch",
        "USER_ADMIN_INVALID": "UserAdminInvalid",
        "USER_ALREADY_PARTICIPANT": "UserAlreadyParticipant",
        "USER_BANNED_IN_CHANNEL": "UserBannedInChannel",
        "USER_BLOCKED": "UserBlocked",
        "USER_BOT": "UserBot",
        "USER_BOT_INVALID": "UserBotInvalid",
        "USER_BOT_REQUIRED": "UserBotRequired",
        "USER_CHANNELS_TOO_MUCH": "UserChannelsTooMuch",
        "USER_CREATOR": "UserCreator",
        "USER_ID_INVALID": "UserIdInvalid",
        "USER_INVALID": "UserInvalid",
        "USER_IS_BLOCKED": "UserIsBlocked",
        "USER_IS_BOT": "UserIsBot",
        "USER_KICKED": "UserKicked",
        "USER_NOT_MUTUAL_CONTACT": "UserNotMutualContact",
        "USER_NOT_PARTICIPANT": "UserNotParticipant",
        "VIDEO_CONTENT_TYPE_INVALID": "VideoContentTypeInvalid",
        "VIDEO_FILE_INVALID": "VideoFileInvalid",
        "VOLUME_LOC_NOT_FOUND": "VolumeLocNotFound",
        "WALLPAPER_FILE_INVALID": "WallpaperFileInvalid",
        "WALLPAPER_INVALID": "WallpaperInvalid",
        "WALLPAPER_MIME_INVALID": "WallpaperMimeInvalid",
        "WC_CONVERT_URL_INVALID": "WcConvertUrlInvalid",
        "WEBDOCUMENT_INVALID": "WebdocumentInvalid",
        "WEBDOCUMENT_MIME_INVALID": "WebdocumentMimeInvalid",
        "WEBDOCUMENT_SIZE_TOO_BIG": "WebdocumentSizeTooBig",
        "WEBDOCUMENT_URL_EMPTY": "WebdocumentUrlEmpty",
        "WEBDOCUMENT_URL_INVALID": "WebdocumentUrlInvalid",
        "WEBPAGE_CURL_FAILED": "WebpageCurlFailed",
        "WEBPAGE_MEDIA_EMPTY": "WebpageMediaEmpty",
        "YOU_BLOCKED_USER": "YouBlockedUser",
        "ENTITY_BOUNDS_INVALID": "EntityBoundsInvalid",
    },
    503: {
        "_": "ServiceUnavailable",
        "ApiCallError": "ApiCallError",
        "Timeout": "Timeout",
    },
    406: {
        "_": "NotAcceptable",
        "AUTH_KEY_DUPLICATED": "AuthKeyDuplicated",
        "CHANNEL_PRIVATE": "ChannelPrivate",
        "FILEREF_UPGRADE_NEEDED": "FilerefUpgradeNeeded",
        "FRESH_CHANGE_ADMINS_FORBIDDEN": "FreshChangeAdminsForbidden",
        "FRESH_CHANGE_PHONE_FORBIDDEN": "FreshChangePhoneForbidden",
        "FRESH_RESET_AUTHORISATION_FORBIDDEN": "FreshResetAuthorisationForbidden",
        "PHONE_NUMBER_INVALID": "PhoneNumberInvalid",
        "PHONE_PASSWORD_FLOOD": "PhonePasswordFlood",
        "STICKERSET_INVALID": "StickersetInvalid",
        "STICKERSET_OWNER_ANONYMOUS": "StickersetOwnerAnonymous",
        "USERPIC_UPLOAD_REQUIRED": "UserpicUploadRequired",
        "USER_RESTRICTED": "UserRestricted",
    },
    303: {
        "_": "SeeOther",
        "FILE_MIGRATE_X": "FileMigrate",
        "NETWORK_MIGRATE_X": "NetworkMigrate",
        "PHONE_MIGRATE_X": "PhoneMigrate",
        "STATS_MIGRATE_X": "StatsMigrate",
        "USER_MIGRATE_X": "UserMigrate",
    },
    500: {
        "_": "InternalServerError",
        "API_CALL_ERROR": "ApiCallError",
        "AUTH_RESTART": "AuthRestart",
        "CALL_OCCUPY_FAILED": "CallOccupyFailed",
        "CHAT_ID_GENERATE_FAILED": "ChatIdGenerateFailed",
        "CHAT_OCCUPY_LOC_FAILED": "ChatOccupyLocFailed",
        "CHAT_OCCUPY_USERNAME_FAILED": "ChatOccupyUsernameFailed",
        "CHP_CALL_FAIL": "ChpCallFail",
        "ENCRYPTION_OCCUPY_ADMIN_FAILED": "EncryptionOccupyAdminFailed",
        "ENCRYPTION_OCCUPY_FAILED": "EncryptionOccupyFailed",
        "FOLDER_DEAC_AUTOFIX_ALL": "FolderDeacAutofixAll",
        "GROUPCALL_ADD_PARTICIPANTS_FAILED": "GroupcallAddParticipantsFailed",
        "GROUPED_ID_OCCUPY_FAILED": "GroupedIdOccupyFailed",
        "HISTORY_GET_FAILED": "HistoryGetFailed",
        "IMAGE_ENGINE_DOWN": "ImageEngineDown",
        "INTERDC_X_CALL_ERROR": "InterdcCallError",
        "INTERDC_X_CALL_RICH_ERROR": "InterdcCallRichError",
        "MEMBER_FETCH_FAILED": "MemberFetchFailed",
        "MEMBER_NO_LOCATION": "MemberNoLocation",
        "MEMBER_OCCUPY_PRIMARY_LOC_FAILED": "MemberOccupyPrimaryLocFailed",
        "MEMBER_OCCUPY_USERNAME_FAILED": "MemberOccupyUsernameFailed",
        "MSGID_DECREASE_RETRY": "MsgidDecreaseRetry",
        "MSG_RANGE_UNSYNC": "MsgRangeUnsync",
        "MT_SEND_QUEUE_TOO_LONG": "MtSendQueueTooLong",
        "NEED_CHAT_INVALID": "NeedChatInvalid",
        "NEED_MEMBER_INVALID": "NeedMemberInvalid",
        "No workers running": "NoWorkersRunning",
        "PARTICIPANT_CALL_FAILED": "ParticipantCallFailed",
        "PERSISTENT_TIMESTAMP_OUTDATED": "PersistentTimestampOutdated",
        "PHOTO_CREATE_FAILED": "PhotoCreateFailed",
        "POSTPONED_TIMEOUT": "PostponedTimeout",
        "PTS_CHANGE_EMPTY": "PtsChangeEmpty",
        "RANDOM_ID_DUPLICATE": "RandomIdDuplicate",
        "REG_ID_GENERATE_FAILED": "RegIdGenerateFailed",
        "RPC_CALL_FAIL": "RpcCallFail",
        "RPC_CONNECT_FAILED": "RpcConnectFailed",
        "RPC_MCGET_FAIL": "RpcMcgetFail",
        "SIGN_IN_FAILED": "SignInFailed",
        "STORAGE_CHECK_FAILED": "StorageCheckFailed",
        "STORE_INVALID_SCALAR_TYPE": "StoreInvalidScalarType",
        "UNKNOWN_METHOD": "UnknownMethod",
        "UPLOAD_NO_VOLUME": "UploadNoVolume",
        "VOLUME_LOC_NOT_FOUND": "VolumeLocNotFound",
        "WORKER_BUSY_TOO_LONG_RETRY": "WorkerBusyTooLongRetry",
        "WP_ID_GENERATE_FAILED": "WpIdGenerateFailed",
    },
}
