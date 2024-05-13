package com.riigess.mona.discord

class Permissions(input:Float) {
    val viewChannels:Boolean
    val manageChannels:Boolean
    val manageRoles:Boolean
    val createExpressions:Boolean
    val manageExpressions:Boolean
    val viewAuditLog:Boolean
    val manageWebhooks:Boolean
    val manageServer:Boolean
    val createInvite:Boolean
    val changeNickname:Boolean
    val manageNicknames:Boolean
    val kickMembers:Boolean
    val banMembers:Boolean
    val timeoutMembers:Boolean
    val sendMessages:Boolean
    val sendMessagesInThreads:Boolean
    val createPublicThreads:Boolean
    val embedLinks:Boolean
    val attachFiles:Boolean
    val addReactions:Boolean
    val useExternalEmoji:Boolean
    val useExternalStickers:Boolean
    val mentionEveryoneOrHere:Boolean
    val manageMessages:Boolean
    val manageThreads:Boolean
    val readMessageHistory:Boolean
    val sendTTSMessages:Boolean
    val useAppCommands:Boolean
    val sendVoiceMessages:Boolean
    val createPolls:Boolean
    val voiceConnect:Boolean
    val voiceSpeak:Boolean
    val voiceVideo:Boolean
    val voiceUseActivities:Boolean
    val voiceUseSoundboard:Boolean
    val voiceUseExternalSounds:Boolean
    val voiceActivity:Boolean
    val voicePrioritySpeaker:Boolean
    val voiceMuteMembers:Boolean
    val voiceDeafenMembers:Boolean
    val voiceMoveMembers:Boolean
    val voiceSetChannelStatus:Boolean
    val createEvents:Boolean
    val manageEvents:Boolean
    val isAdministrator:Boolean

    init {
        this.viewChannels = (input % 1024f == 0f)
        this.manageChannels = (input % 16f == 0f)
        this.manageRoles
        this.createExpressions
        this.manageExpressions
        this.viewAuditLog
        this.manageWebhooks
        this.manageServer
        this.createInvite
        this.changeNickname
        this.manageNicknames
        this.kickMembers
        this.banMembers
        this.timeoutMembers
        this.sendMessages
        this.sendMessagesInThreads
        this.createPublicThreads
        this.embedLinks
        this.attachFiles
        this.addReactions
        this.useExternalEmoji
        this.useExternalStickers
        this.mentionEveryoneOrHere
        this.manageMessages
        this.manageThreads
        this.readMessageHistory
        this.sendTTSMessages
        this.useAppCommands
        this.sendVoiceMessages
        this.createPolls
        this.voiceConnect
        this.voiceSpeak
        this.voiceVideo
        this.voiceUseActivities
        this.voiceUseSoundboard
        this.voiceUseExternalSounds
        this.voiceActivity
        this.voicePrioritySpeaker
        this.voiceMuteMembers
        this.voiceDeafenMembers
        this.voiceMoveMembers
        this.voiceSetChannelStatus
        this.createEvents
        this.manageEvents
        this.isAdministrator
    }
}