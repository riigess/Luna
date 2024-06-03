package com.riigess.mona.discord

open class Permissions(input:Int) {
    open val viewChannels:Boolean
    open val manageChannels:Boolean
    open val manageRoles:Boolean
    open val createExpressions:Boolean
    open val manageExpressions:Boolean
    open val viewAuditLog:Boolean
    open val manageWebhooks:Boolean
    open val manageServer:Boolean
    open val createInvite:Boolean
    open val changeNickname:Boolean
    open val manageNicknames:Boolean
    open val kickMembers:Boolean
    open val banMembers:Boolean
    open val timeoutMembers:Boolean
    open val sendMessages:Boolean
    open val sendMessagesInThreads:Boolean
    open val createPublicThreads:Boolean
    open val embedLinks:Boolean
    open val attachFiles:Boolean
    open val addReactions:Boolean
    open val useExternalEmoji:Boolean
    open val useExternalStickers:Boolean
    open val mentionEveryoneOrHere:Boolean
    open val manageMessages:Boolean
    open val manageThreads:Boolean
    open val readMessageHistory:Boolean
    open val sendTTSMessages:Boolean
    open val useAppCommands:Boolean
    open val sendVoiceMessages:Boolean
    open val createPolls:Boolean
    open val voiceConnect:Boolean
    open val voiceSpeak:Boolean
    open val voiceVideo:Boolean
    open val voiceUseActivities:Boolean
    open val voiceUseSoundboard:Boolean
    open val voiceUseExternalSounds:Boolean
    open val voiceActivity:Boolean
    open val voicePrioritySpeaker:Boolean
    open val voiceMuteMembers:Boolean
    open val voiceDeafenMembers:Boolean
    open val voiceMoveMembers:Boolean
//    open val voiceSetChannelStatus:Boolean
    open val createEvents:Boolean
    open val manageEvents:Boolean
    open val isAdministrator:Boolean
    open val raw:Int

    init {
        this.createInvite = input and (1 shl 0) == (1 shl 0)
        this.kickMembers = input and (1 shl 1) == (1 shl 1)
        this.banMembers = input and (1 shl 2) == (1 shl 2)
        this.isAdministrator = input and (1 shl 3) == (1 shl 3)
        this.manageChannels = input and (1 shl 4) == (1 shl 4)
        this.manageServer = input and (1 shl 5) == (1 shl 5)
        this.addReactions = input and (1 shl 6) == (1 shl 6)
        this.viewAuditLog = input and (1 shl 7) == (1 shl 7)
        this.voicePrioritySpeaker = input and (1 shl 8) == (1 shl 8)
        this.voiceVideo = input and (1 shl 9) == (1 shl 9)
        this.viewChannels = input and (1 shl 10) == (1 shl 10)
        this.sendMessages = input and (1 shl 11) == (1 shl 11)
        this.sendTTSMessages = input and (1 shl 12) == (1 shl 12)
        this.manageMessages = input and (1 shl 13) == (1 shl 13)
        this.embedLinks = input and (1 shl 14) == (1 shl 14)
        this.attachFiles = input and (1 shl 15) == (1 shl 15)
        this.readMessageHistory = input and (1 shl 16) == (1 shl 16)
        this.mentionEveryoneOrHere = input and (1 shl 17) == (1 shl 17)
        this.useExternalEmoji = input and (1 shl 18) == (1 shl 18)
//        this.insights = input and (1 shl 19) == (1 shl 19)
        this.voiceConnect = input and (1 shl 20) == (1 shl 20)
        this.voiceSpeak = input and (1 shl 21) == (1 shl 21)
        this.voiceMuteMembers = input and (1 shl 22) == (1 shl 22)
        this.voiceDeafenMembers = input and (1 shl 23) == (1 shl 23)
        this.voiceMoveMembers = input and (1 shl 24) == (1 shl 24)
        this.voiceActivity = input and (1 shl 25) == (1 shl 25)
        this.changeNickname = input and (1 shl 26) == (1 shl 26)
        this.manageNicknames = input and (1 shl 27) == (1 shl 27)
        this.manageRoles = input and (1 shl 28) == (1 shl 28)
        this.manageWebhooks = input and (1 shl 29) == (1 shl 29)
        this.manageExpressions = input and (1 shl 30) == (1 shl 30)
        this.useAppCommands = input and (1 shl 31) == (1 shl 31)
//        this.voiceRequestToSpeak = input and (1 shl 32) == (1 shl 32)
        this.manageEvents = input and (1 shl 33) == (1 shl 33)
        this.manageThreads = input and (1 shl 34) == (1 shl 34)
        this.createPublicThreads = input and (1 shl 35) == (1 shl 35)
//        this.createPrivateThreads = input and (1 shl 36) == (1 shl 36)
        this.useExternalStickers = input and (1 shl 37) == (1 shl 37)
        this.sendMessagesInThreads = input and (1 shl 38) == (1 shl 38)
        this.voiceUseActivities = input and (1 shl 39) == (1 shl 39)
        this.timeoutMembers = input and (1 shl 40) == (1 shl 40)
//        this.viewCreatorMonetizationAnalytics = input and (1 shl 41) == (1 shl 41)
        this.voiceUseSoundboard = input and (1 shl 42) == (1 shl 42)
        this.createExpressions = input and (1 shl 43) == (1 shl 43)
        this.createEvents = input and (1 shl 44) == (1 shl 44)
        this.voiceUseExternalSounds = input and (1 shl 45) == (1 shl 45)
        this.sendVoiceMessages = input and (1 shl 46) == (1 shl 46)
        this.createPolls = input and (1 shl 49) == (1 shl 49)
        this.raw = input
    }

    fun getInt(): Int {
        return this.raw
    }
}