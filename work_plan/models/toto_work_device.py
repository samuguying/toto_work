from odoo import models, fields, api


class WorkDevice(models.Model):
    _name = 'toto.work.device'

    name = fields.Char('设备名称', required=True)
    device_type = fields.Selection([('shaping', '成形系'),
                                    ('power', '动力系'),
                                    ('process', '加工系'),
                                    ('dissolve', '溶着系'),
                                    ('other', '其他')], '类型', default='other', required=True)

    _sql_constraints = [
        ("name_uniq", "unique (name)", "名称不能重复！"),
    ]

    @api.model
    def default_get(self, fields_list):
        res = super(WorkDevice, self).default_get(fields_list)
        if self.user_has_groups("work_plan.group_work_plan_manager"):
            res.update({'device_type': None})
        elif self.user_has_groups("work_plan.group_work_shaping_monitor"):
            res.update({'device_type': 'shaping'})
        elif self.user_has_groups("work_plan.group_work_power_monitor"):
            res.update({'device_type': 'power'})
        elif self.user_has_groups("work_plan.group_work_process_monitor"):
            res.update({'device_type': 'process'})
        elif self.user_has_groups("work_plan.group_work_dissolve_monitor"):
            res.update({'device_type': 'dissolve'})
        else:
            res.update({'device_type': None})
        return res
