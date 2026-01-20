# -*- coding: utf-8 -*-

import pdb
from odoo import models, fields, api


class BlogEntry(models.Model):
    _name = "blog.entry"  # blog_entry -> Nombre de la tabla
    _description = "Blog entries for my blog"

    title = fields.Char(name="Title", required=True)
    content = fields.Html(name="Content", required=True)
    author_id = fields.Many2one(
        name="Author",
        comodel_name="res.users",
        required=True,
        default=lambda self: self.env.user,
        readonly=True
    )
    create_date = fields.Datetime(
        name="Create Date", required=True, 
        default=fields.Datetime.now
    )
    slug = fields.Char(name="Slug", compute="_compute_slug_from_title")
    tag_ids = fields.Many2many(name="Tags", comodel_name="blog.tag")
    
    @api.depends("title", "create_date")
    def _compute_slug_from_title(self):
        for record in self:
            record.slug = record.title.replace(" ", "-") + "-" + record.create_date.strftime("%Y%m%d")

    @api.onchange("title")
    def _onchange_title(self):
        title_arr = self.title.split(" ")
        for title_word in title_arr:
            self.tag_ids.create({
                "name": title_word
            })

    def get_title_date(self):
        return f"{self.title} {self.create_date}"


class BlogTag(models.Model):
    _name = "blog.tag"
    _description = "Tags for entry blogs"

    name = fields.Char(name="Name", required=True)