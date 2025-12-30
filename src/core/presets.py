"""
Presets - Optimized setting presets for different playstyles.
Based on V2.0 presets with competitive gaming optimizations.
"""

from typing import Dict, Any

PRESETS = {
    'esports': {
        'name': 'Esports Pro',
        'icon': '🏆',
        'color': '#e53935',
        'description': 'Maximum competitive advantage - used by pro players. Lowest settings, highest FPS.',
        'settings': {
            'GstRender.Dx12Enabled': '1',
            'GstRender.FullscreenMode': '2',
            'GstRender.VSyncMode': '0',
            'GstRender.FutureFrameRendering': '1',
            'GstRender.FrameRateLimit': '0.000000',
            'GstRender.FrameRateLimiterEnable': '0',
            'GstRender.OverallGraphicsQuality': '0',
            'GstRender.TextureQuality': '0',
            'GstRender.TextureFiltering': '0',
            'GstRender.ShadowQuality': '0',
            'GstRender.EffectsQuality': '0',
            'GstRender.LightingQuality': '0',
            'GstRender.PostProcessQuality': '0',
            'GstRender.MeshQuality': '0',
            'GstRender.TerrainQuality': '0',
            'GstRender.VegetationQuality': '0',
            'GstRender.VolumetricQuality': '0',
            'GstRender.AntiAliasingDeferred': '0',
            'GstRender.AmbientOcclusion': '0',
            'GstRender.ScreenSpaceReflections': '0',
            'GstRender.MotionBlurEnable': '0',
            'GstRender.MotionBlurWorld': '0.000000',
            'GstRender.MotionBlurWeapon': '0.000000',
            'GstRender.DepthOfFieldEnable': '0',
            'GstRender.WeaponDOF': '0',
            'GstRender.FilmGrain': '0',
            'GstRender.LensDistortion': '0',
            'GstRender.ChromaticAberration': '0',
            'GstRender.Vignette': '0',
            'GstRender.ResolutionScale': '1.000000',
            'GstRender.NvidiaLowLatency': '2',
            'GstRender.RaytracingAmbientOcclusion': '0',
            'GstRender.RaytracingReflections': '0',
            'GstRender.RaytracingGlobalIllumination': '0',
            'GstAudio.HitIndicatorSound': '1',
            'GstAudio.SubtitlesEnemies': '1',
            'GstAudio.SubtitlesFriendlies': '1',
            'GstAudio.SubtitlesSquad': '1',
            'GstInput.MouseRawInput': '1',
            'GstInput.UniformSoldierAiming': '1',
        }
    },
    'competitive': {
        'name': 'Competitive',
        'icon': '🎯',
        'color': '#fb8c00',
        'description': 'Balanced for competitive play. Good FPS with acceptable visuals.',
        'settings': {
            'GstRender.Dx12Enabled': '1',
            'GstRender.FullscreenMode': '2',
            'GstRender.VSyncMode': '0',
            'GstRender.FutureFrameRendering': '1',
            'GstRender.FrameRateLimit': '0.000000',
            'GstRender.FrameRateLimiterEnable': '0',
            'GstRender.OverallGraphicsQuality': '1',
            'GstRender.TextureQuality': '2',
            'GstRender.TextureFiltering': '2',
            'GstRender.ShadowQuality': '1',
            'GstRender.EffectsQuality': '1',
            'GstRender.LightingQuality': '1',
            'GstRender.PostProcessQuality': '0',
            'GstRender.MeshQuality': '1',
            'GstRender.TerrainQuality': '1',
            'GstRender.VegetationQuality': '0',
            'GstRender.VolumetricQuality': '0',
            'GstRender.AntiAliasingDeferred': '2',
            'GstRender.AmbientOcclusion': '0',
            'GstRender.ScreenSpaceReflections': '0',
            'GstRender.MotionBlurEnable': '0',
            'GstRender.MotionBlurWorld': '0.000000',
            'GstRender.MotionBlurWeapon': '0.000000',
            'GstRender.DepthOfFieldEnable': '0',
            'GstRender.WeaponDOF': '0',
            'GstRender.FilmGrain': '0',
            'GstRender.LensDistortion': '0',
            'GstRender.ChromaticAberration': '0',
            'GstRender.Vignette': '0',
            'GstRender.ResolutionScale': '1.000000',
            'GstRender.NvidiaLowLatency': '2',
            'GstInput.MouseRawInput': '1',
            'GstInput.UniformSoldierAiming': '1',
        }
    },
    'balanced': {
        'name': 'Balanced',
        'icon': '⚖️',
        'color': '#43a047',
        'description': 'Good mix of performance and visuals. Recommended for most players.',
        'settings': {
            'GstRender.Dx12Enabled': '1',
            'GstRender.FullscreenMode': '1',
            'GstRender.VSyncMode': '0',
            'GstRender.FutureFrameRendering': '1',
            'GstRender.FrameRateLimit': '144.000000',
            'GstRender.FrameRateLimiterEnable': '1',
            'GstRender.OverallGraphicsQuality': '2',
            'GstRender.TextureQuality': '2',
            'GstRender.TextureFiltering': '2',
            'GstRender.ShadowQuality': '2',
            'GstRender.EffectsQuality': '2',
            'GstRender.LightingQuality': '2',
            'GstRender.PostProcessQuality': '2',
            'GstRender.MeshQuality': '2',
            'GstRender.TerrainQuality': '2',
            'GstRender.VegetationQuality': '2',
            'GstRender.VolumetricQuality': '1',
            'GstRender.AntiAliasingDeferred': '5',
            'GstRender.AmbientOcclusion': '1',
            'GstRender.ScreenSpaceReflections': '1',
            'GstRender.MotionBlurEnable': '0',
            'GstRender.MotionBlurWorld': '0.000000',
            'GstRender.MotionBlurWeapon': '0.000000',
            'GstRender.DepthOfFieldEnable': '0',
            'GstRender.FilmGrain': '0',
            'GstRender.LensDistortion': '0',
            'GstRender.ChromaticAberration': '0',
            'GstRender.Vignette': '0',
            'GstRender.ResolutionScale': '1.000000',
            'GstRender.NvidiaLowLatency': '1',
        }
    },
    'quality': {
        'name': 'Quality',
        'icon': '✨',
        'color': '#1e88e5',
        'description': 'High visual quality for powerful systems. Best for screenshots and singleplayer.',
        'settings': {
            'GstRender.Dx12Enabled': '1',
            'GstRender.FullscreenMode': '1',
            'GstRender.VSyncMode': '1',
            'GstRender.FutureFrameRendering': '1',
            'GstRender.FrameRateLimit': '60.000000',
            'GstRender.FrameRateLimiterEnable': '1',
            'GstRender.OverallGraphicsQuality': '3',
            'GstRender.TextureQuality': '3',
            'GstRender.TextureFiltering': '3',
            'GstRender.ShadowQuality': '3',
            'GstRender.EffectsQuality': '3',
            'GstRender.LightingQuality': '3',
            'GstRender.PostProcessQuality': '3',
            'GstRender.MeshQuality': '3',
            'GstRender.TerrainQuality': '3',
            'GstRender.VegetationQuality': '3',
            'GstRender.VolumetricQuality': '3',
            'GstRender.AntiAliasingDeferred': '7',
            'GstRender.AmbientOcclusion': '1',
            'GstRender.ScreenSpaceReflections': '1',
            'GstRender.MotionBlurEnable': '1',
            'GstRender.MotionBlurWorld': '50.000000',
            'GstRender.MotionBlurWeapon': '25.000000',
            'GstRender.DepthOfFieldEnable': '1',
            'GstRender.WeaponDOF': '1',
            'GstRender.FilmGrain': '0',
            'GstRender.LensDistortion': '0',
            'GstRender.ChromaticAberration': '0',
            'GstRender.Vignette': '0',
            'GstRender.ResolutionScale': '1.000000',
            'GstRender.RaytracingAmbientOcclusion': '1',
            'GstRender.RaytracingReflections': '1',
        }
    },
    'ultra': {
        'name': 'Ultra Quality',
        'icon': '💎',
        'color': '#8e24aa',
        'description': 'Maximum visual quality. Requires high-end hardware (RTX 4080+).',
        'settings': {
            'GstRender.Dx12Enabled': '1',
            'GstRender.FullscreenMode': '2',
            'GstRender.VSyncMode': '1',
            'GstRender.FutureFrameRendering': '1',
            'GstRender.FrameRateLimit': '0.000000',
            'GstRender.FrameRateLimiterEnable': '0',
            'GstRender.OverallGraphicsQuality': '4',
            'GstRender.TextureQuality': '4',
            'GstRender.TextureFiltering': '4',
            'GstRender.ShadowQuality': '3',
            'GstRender.EffectsQuality': '3',
            'GstRender.LightingQuality': '3',
            'GstRender.PostProcessQuality': '3',
            'GstRender.MeshQuality': '3',
            'GstRender.TerrainQuality': '3',
            'GstRender.VegetationQuality': '3',
            'GstRender.VolumetricQuality': '3',
            'GstRender.AntiAliasingDeferred': '8',
            'GstRender.AmbientOcclusion': '1',
            'GstRender.ScreenSpaceReflections': '1',
            'GstRender.MotionBlurEnable': '1',
            'GstRender.MotionBlurWorld': '50.000000',
            'GstRender.MotionBlurWeapon': '25.000000',
            'GstRender.DepthOfFieldEnable': '1',
            'GstRender.WeaponDOF': '1',
            'GstRender.FilmGrain': '0',
            'GstRender.ResolutionScale': '1.000000',
            'GstRender.RaytracingAmbientOcclusion': '1',
            'GstRender.RaytracingReflections': '1',
            'GstRender.RaytracingGlobalIllumination': '1',
            'GstRender.NVIDIAFrameGenerationEnabled': '1',
        }
    },
}


def apply_preset(config_manager, preset_key: str) -> tuple[bool, str]:
    """Apply a preset to the config manager."""
    if preset_key not in PRESETS:
        return False, f"Unknown preset: {preset_key}"
    
    preset = PRESETS[preset_key]
    success, message = config_manager.update(preset['settings'])
    
    if success:
        return True, f"Applied '{preset['name']}' preset ({len(preset['settings'])} settings)"
    return False, message


def get_preset_names() -> list:
    """Get list of available preset names."""
    return list(PRESETS.keys())


def get_preset_info(preset_key: str) -> Dict[str, Any]:
    """Get info about a specific preset."""
    return PRESETS.get(preset_key, {})
