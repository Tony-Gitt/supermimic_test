"""Environment configuration checks."""

from supermimic.tasks.env_cfgs import gencoord_env_cfg, maxcoord_env_cfg


def test_supermimic_uses_full_mujoco_solver_budgets():
  for cfg in (gencoord_env_cfg(), maxcoord_env_cfg()):
    # The base tracking task uses 10 and 20, which triggers MuJoCo-Warp
    # overflow warnings on harder reference motions.
    assert cfg.sim.mujoco.iterations > 10
    assert cfg.sim.mujoco.ls_iterations > 20
