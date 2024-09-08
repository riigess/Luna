val ktor_version: String by project
val org_json_version: String by project

plugins {
    application
    kotlin("jvm") version "1.9.23"
    id("com.google.protobuf") version "0.8.13"
}

group = "org.example"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
    maven { url = uri("https://maven.pkg.jetbrains.space/public/p/ktor/eap")}

    maven("https://repo.kord.dev/snapshots")
    maven("https://oss.sonatype.org/content/repositories/snapshots")
}

dependencies {
    testImplementation(kotlin("test"))
    implementation("com.squareup.okhttp3:okhttp:4.12.0")
    implementation("com.beust:klaxon:5.5")
    implementation("io.ktor:ktor-client-core:$ktor_version")
    implementation("io.ktor:ktor-client-cio:$ktor_version")
    implementation("io.ktor:ktor-client-websockets:$ktor_version")
    implementation("org.json:json:$org_json_version")
    implementation("org.slf4j:slf4j-simple:2.0.13")
    implementation("org.slf4j:slf4j-api:2.0.13")
    implementation("io.insert-koin:koin-java:2.0.1")
    //TODO: Get twitch API library (or, better yet, an IRC library)
    //TODO: Get a web API library (will SpringFramework work?)
    //Discord library (Kord - https://github.com/kordlib/kord)
    implementation("dev.kord:kord-core:0.14.0")
}

application {
    mainClass = "com.riigess.mona.Runner"
}

tasks.test {
    useJUnitPlatform()
}
kotlin {
    jvmToolchain(21)
}